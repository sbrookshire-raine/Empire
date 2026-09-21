"""Original dependency-free CLI and limited MCP 2025-11-25 stdio server."""
import argparse
import json
import math
import os
import sys
import time
from . import kernel

VERSION = '0.1.0'
NAME = 'scenario-regret'
PROTOCOL = '2025-11-25'
MAX_BYTES = 262144
MAX_DEPTH = 32


def offline_guard(event, args):
    if event.startswith('socket.') or event in ('urllib.Request', 'http.client.connect'):
        raise PermissionError('network access is disabled')


sys.addaudithook(offline_guard)


def dumps(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(',', ':'), allow_nan=False)


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError('duplicate JSON object key')
        result[key] = value
    return result


def parse(raw):
    if len(raw) > MAX_BYTES:
        raise ValueError('input exceeds 262144 bytes')
    text = raw.decode('utf-8', errors='strict')
    level = 0
    quoted = escaped = False
    for char in text:
        if quoted:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == '"':
                quoted = False
        elif char == '"':
            quoted = True
        elif char in '[{':
            level += 1
            if level > MAX_DEPTH:
                raise ValueError('JSON nesting exceeds 32 levels')
        elif char in ']}':
            level -= 1
    def bad_constant(_):
        raise ValueError('nonfinite JSON number')
    return json.loads(text, object_pairs_hook=pairs, parse_constant=bad_constant)


def check(schema, value, at='input'):
    """Validate only the documented JSON Schema subset used by these packages."""
    typ = schema.get('type')
    allowed = {'object': isinstance(value, dict), 'array': isinstance(value, list),
               'string': isinstance(value, str), 'number': type(value) in (int, float),
               'integer': type(value) is int, 'boolean': type(value) is bool,
               'null': value is None}
    if typ and not (any(allowed.get(t, False) for t in typ) if isinstance(typ, list) else allowed.get(typ, False)):
        raise ValueError(at + ': invalid type')
    if type(value) in (int, float):
        try:
            finite = math.isfinite(value)
        except OverflowError:
            finite = False
        if not finite:
            raise ValueError(at + ': number must be finite')
        if 'minimum' in schema and value < schema['minimum']:
            raise ValueError(at + ': below minimum')
        if 'maximum' in schema and value > schema['maximum']:
            raise ValueError(at + ': above maximum')
        if 'exclusiveMinimum' in schema and value <= schema['exclusiveMinimum']:
            raise ValueError(at + ': below exclusive minimum')
        if 'exclusiveMaximum' in schema and value >= schema['exclusiveMaximum']:
            raise ValueError(at + ': above exclusive maximum')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(at + ': invalid enum value')
    if isinstance(value, str):
        if not schema.get('minLength', 0) <= len(value) <= schema.get('maxLength', MAX_BYTES):
            raise ValueError(at + ': invalid string length')
        if 'pattern' in schema:
            import re
            if re.search(schema['pattern'], value) is None:
                raise ValueError(at + ': invalid string pattern')
    if isinstance(value, dict):
        props = schema.get('properties', {})
        if any(key not in value for key in schema.get('required', [])):
            raise ValueError(at + ': missing required field')
        if schema.get('additionalProperties') is False and any(key not in props for key in value):
            raise ValueError(at + ': unexpected field')
        for key, child in value.items():
            if key in props:
                check(props[key], child, at + '.' + key)
            elif isinstance(schema.get('additionalProperties'), dict):
                check(schema['additionalProperties'], child, at + '.*')
    if isinstance(value, list):
        if not schema.get('minItems', 0) <= len(value) <= schema.get('maxItems', MAX_BYTES):
            raise ValueError(at + ': invalid array length')
        if schema.get('uniqueItems') and len({dumps(x) for x in value}) != len(value):
            raise ValueError(at + ': duplicate array items')
        for child in value:
            if 'items' in schema:
                check(schema['items'], child, at + '[]')


def calculate(value):
    check(kernel.SCHEMA, value)
    result = kernel.run(value)
    encoded = dumps(result)
    if len(encoded) > MAX_BYTES:
        raise ValueError('result exceeds output budget')
    return result


def error(code, message, ident=None):
    return {'jsonrpc':'2.0', 'id':ident, 'error':{'code':code, 'message':message}}


def success(ident, result):
    return {'jsonrpc':'2.0', 'id':ident, 'result':result}


class Server:
    def __init__(self):
        self.state = 'new'
        self.tokens = 20.0
        self.last_call = time.monotonic()

    def rate_allowed(self):
        now = time.monotonic()
        self.tokens = min(20.0, self.tokens + (now - self.last_call) * 10.0)
        self.last_call = now
        if self.tokens < 1.0:
            return False
        self.tokens -= 1.0
        return True

    def handle(self, req):
        if not isinstance(req, dict) or req.get('jsonrpc') != '2.0':
            return error(-32600, 'Invalid request')
        ident = req.get('id')
        notification = 'id' not in req
        if not notification and not (type(ident) is int or isinstance(ident, str)):
            return error(-32600, 'Invalid request ID')
        if not notification and ((isinstance(ident, str) and len(ident) > 128)
                                 or (type(ident) is int and abs(ident) > 9007199254740991)):
            return error(-32600, 'Request ID exceeds supported bounds')
        if not isinstance(req.get('method'), str) or len(req['method']) > 128:
            return error(-32600, 'Invalid method', ident)
        method = req['method']
        params = req.get('params', {})
        if not isinstance(params, dict):
            return None if notification else error(-32602, 'Parameters must be an object', ident)
        if notification:
            if method == 'notifications/initialized' and self.state == 'initialized':
                self.state = 'ready'
            return None
        if method == 'ping':
            return success(ident, {})
        if method == 'initialize':
            if self.state != 'new':
                return error(-32600, 'Already initialized', ident)
            if (not isinstance(params.get('protocolVersion'), str)
                or not isinstance(params.get('capabilities'), dict)
                or not isinstance(params.get('clientInfo'), dict)
                or not isinstance(params['clientInfo'].get('name'), str)
                or not isinstance(params['clientInfo'].get('version'), str)):
                return error(-32602, 'Invalid initialization parameters', ident)
            self.state = 'initialized'
            # Legacy negotiation: offer our supported revision; client must reject if unsupported.
            return success(ident, {'protocolVersion':PROTOCOL, 'capabilities':{'tools':{'listChanged':False}},
                                   'serverInfo':{'name':NAME, 'version':VERSION}})
        if method not in ('tools/list', 'tools/call'):
            return error(-32601, 'Method not found; supports legacy MCP 2025-11-25', ident)
        if self.state != 'ready':
            return error(-32600, 'Initialize and send notifications/initialized first', ident)
        if method == 'tools/list':
            if 'cursor' in params:
                return error(-32602, 'Pagination is not supported', ident)
            return success(ident, {'tools':[{'name':NAME.replace('-', '_'), 'description':kernel.__doc__.strip(),
                 'inputSchema':kernel.SCHEMA, 'outputSchema':{'type':'object'},
                 'annotations':{'readOnlyHint':True, 'destructiveHint':False, 'idempotentHint':True, 'openWorldHint':False}}]})
        if params.get('name') != NAME.replace('-', '_'):
            return error(-32602, 'Unknown tool', ident)
        if not self.rate_allowed():
            return success(ident, {'content':[{'type':'text', 'text':'rate limit: retry after 0.1 seconds'}], 'isError':True})
        try:
            result = calculate(params.get('arguments', {}))
        except (ValueError, TypeError, OverflowError, RecursionError) as exc:
            return success(ident, {'content':[{'type':'text', 'text':str(exc)}], 'isError':True})
        return success(ident, {'content':[{'type':'text', 'text':dumps(result)}],
                               'structuredContent':result, 'isError':False})


def serve():
    server = Server()
    while True:
        raw = sys.stdin.buffer.readline(MAX_BYTES + 1)
        if not raw:
            return 0
        if len(raw) > MAX_BYTES:
            print(dumps(error(-32700, 'Frame exceeds 262144 bytes')), flush=True)
            return 2  # Do not drain an unbounded hostile stream.
        try:
            value = parse(raw)
        except (ValueError, UnicodeError, RecursionError):
            response = error(-32700, 'Invalid JSON frame')
        else:
            try:
                response = server.handle(value)
            except Exception:
                response = error(-32603, 'Internal error')
        if response is not None:
            print(dumps(response), flush=True)


def main():
    parser = argparse.ArgumentParser(prog=NAME, description=kernel.__doc__)
    parser.add_argument('--version', action='version', version=VERSION)
    parser.add_argument('command', choices=('run', 'schema', 'mcp'), help='run reads one JSON object from stdin; mcp serves newline-delimited JSON-RPC')
    args = parser.parse_args()
    try:
        if os.environ.get('LOCAL_SKILL_NETWORK', 'deny') != 'deny':
            raise ValueError('LOCAL_SKILL_NETWORK must be deny or unset')
        if args.command == 'schema':
            print(dumps(kernel.SCHEMA))
            return 0
        if args.command == 'mcp':
            return serve()
        raw = sys.stdin.buffer.read(MAX_BYTES + 1)
        result = calculate(parse(raw))
        print(dumps(result))
        return 0
    except (ValueError, TypeError, UnicodeError, OverflowError, RecursionError) as exc:
        print(dumps({'error':{'code':'INVALID_INPUT', 'message':str(exc)}}), file=sys.stderr)
        return 2
    except BrokenPipeError:
        return 3
    except Exception:
        print(dumps({'error':{'code':'INTERNAL_ERROR', 'message':'operation failed'}}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
