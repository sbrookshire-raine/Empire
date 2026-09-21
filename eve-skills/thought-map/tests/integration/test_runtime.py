"""Integration and negative tests against the installed distribution."""
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

runtime = importlib.import_module('local_thought_map.runtime')
kernel = importlib.import_module('local_thought_map.kernel')
NAME = 'thought-map'
MOD = 'local_thought_map'


def call(args, data=b'', env=None):
    return subprocess.run([sys.executable, '-m', MOD, *args], input=data, capture_output=True, timeout=15, env=env)


def rpc(method, ident=1, **params):
    return {'jsonrpc':'2.0','id':ident,'method':method,'params':params}


def initialized():
    return [rpc('initialize', protocolVersion='2025-11-25', capabilities={}, clientInfo={'name':'test','version':'1'}),
            {'jsonrpc':'2.0','method':'notifications/initialized'}]


def session(messages):
    raw = b''.join((json.dumps(x)+'\n').encode() for x in messages)
    result = call(['mcp'], raw)
    return result, [json.loads(x) for x in result.stdout.splitlines()]


class CLI(unittest.TestCase):
    def test_help(self):
        p=call(['--help']); self.assertEqual(p.returncode,0); self.assertIn(b'usage:',p.stdout)
    def test_version(self):
        p=call(['--version']); self.assertEqual(p.returncode,0); self.assertEqual(p.stdout.strip(),b'0.1.0')
    def test_schema(self):
        p=call(['schema']); self.assertEqual(p.returncode,0); self.assertEqual(json.loads(p.stdout),kernel.SCHEMA)
    def test_fixture(self):
        p=call(['run'],json.dumps(kernel.SAMPLE).encode()); self.assertEqual(p.returncode,0,p.stderr)
        self.assertEqual(json.loads(p.stdout),kernel.EXPECTED); self.assertEqual(p.stderr,b'')
    def test_determinism(self):
        raw=json.dumps(kernel.SAMPLE).encode(); self.assertEqual(call(['run'],raw).stdout,call(['run'],raw).stdout)
    def test_malformed(self):
        for raw in (b'',b'{',b'[]',b'null',b'{}',b'42',b'"value"',b'{}{}',b'{"x":NaN}',b'{"x":1,"x":2}',b'\xff',b'{"x":Infinity}',b'['*33+b'0'+b']'*33,b'{"x":1e999}'):
            with self.subTest(raw=raw[:40]):
                p=call(['run'],raw); self.assertEqual(p.returncode,2,p.stderr); self.assertEqual(p.stdout,b'')
                self.assertEqual(json.loads(p.stderr)['error']['code'],'INVALID_INPUT')
    def test_extra_key(self):
        sample=dict(kernel.SAMPLE,unknown='$(touch SHOULD_NOT_EXIST)')
        p=call(['run'],json.dumps(sample).encode()); self.assertEqual(p.returncode,2); self.assertFalse(Path('SHOULD_NOT_EXIST').exists())
    def test_oversized(self):
        p=call(['run'],b' '*262145); self.assertEqual(p.returncode,2)
    def test_unknown_command(self):
        self.assertEqual(call(['not-a-command']).returncode,2)
    def test_missing_path_unsupported(self):
        self.assertEqual(call(['run','--input','/definitely/missing.json']).returncode,2)
    def test_invalid_configuration(self):
        env=dict(os.environ,LOCAL_SKILL_NETWORK='allow')
        p=call(['run'],json.dumps(kernel.SAMPLE).encode(),env); self.assertEqual(p.returncode,2)
    def test_network_guard(self):
        code=f'import {MOD}.runtime; import socket; socket.socket()'
        p=subprocess.run([sys.executable,'-c',code],capture_output=True,timeout=15)
        self.assertNotEqual(p.returncode,0); self.assertIn(b'network access is disabled',p.stderr)


class MCP(unittest.TestCase):
    def test_lifecycle_discovery_call(self):
        messages=initialized()+[rpc('tools/list',2),rpc('tools/call',3,name=NAME.replace('-','_'),arguments=kernel.SAMPLE),rpc('ping',4)]
        p,out=session(messages); self.assertEqual(p.returncode,0,p.stderr); self.assertEqual(p.stderr,b''); self.assertEqual(len(out),4)
        self.assertEqual(out[0]['result']['protocolVersion'],'2025-11-25')
        self.assertEqual(out[1]['result']['tools'][0]['inputSchema'],kernel.SCHEMA)
        self.assertEqual(out[1]['result']['tools'][0]['name'],NAME.replace('-','_'))
        self.assertEqual(out[2]['result']['structuredContent'],kernel.EXPECTED)
        self.assertFalse(out[2]['result']['isError'])
        self.assertEqual(json.loads(out[2]['result']['content'][0]['text']),kernel.EXPECTED)
        self.assertEqual(out[3]['result'],{})
    def test_before_initialize(self):
        p,out=session([rpc('tools/list')]); self.assertEqual(out[0]['error']['code'],-32600)
    def test_before_initialized_notification(self):
        p,out=session(initialized()[:1]+[rpc('tools/list',2)]); self.assertEqual(out[1]['error']['code'],-32600)
    def test_invalid_initialize(self):
        p,out=session([rpc('initialize')]); self.assertEqual(out[0]['error']['code'],-32602)
    def test_version_negotiation(self):
        p,out=session([rpc('initialize',protocolVersion='2099-01-01',capabilities={},clientInfo={'name':'test','version':'1'})])
        self.assertEqual(out[0]['result']['protocolVersion'],'2025-11-25')
    def test_tool_error(self):
        p,out=session(initialized()+[rpc('tools/call',2,name=NAME.replace('-','_'),arguments={})]); self.assertTrue(out[-1]['result']['isError'])
    def test_unknown_tool(self):
        p,out=session(initialized()+[rpc('tools/call',2,name='unknown',arguments={})]); self.assertEqual(out[-1]['error']['code'],-32602)
    def test_invalid_envelopes(self):
        cases=[([], -32600), ({'jsonrpc':'2.0','id':None,'method':'ping'},-32600),
               ({'jsonrpc':'2.0','id':False,'method':'ping'},-32600),
               ({'jsonrpc':'2.0','id':1.5,'method':'ping'},-32600),
               ({'jsonrpc':'2.0','id':1,'method':2},-32600),
               ({'jsonrpc':'2.0','id':1,'method':'ping','params':[]},-32602)]
        for req,code in cases:
            with self.subTest(req=req):
                p,out=session([req]); self.assertEqual(out[0]['error']['code'],code)
    def test_unknown_method(self):
        p,out=session(initialized()+[rpc('server/discover',2)]); self.assertEqual(out[-1]['error']['code'],-32601)
    def test_duplicate_initialize(self):
        p,out=session(initialized()+initialized()[:1]); self.assertEqual(out[-1]['error']['code'],-32600)
    def test_pagination_rejected(self):
        p,out=session(initialized()+[rpc('tools/list',2,cursor='x')]); self.assertEqual(out[-1]['error']['code'],-32602)
    def test_notification_silence(self):
        p,out=session([{'jsonrpc':'2.0','method':'notifications/cancelled','params':{'requestId':1}}]); self.assertEqual(out,[])
    def test_malformed_recovery(self):
        p=call(['mcp'],b'{\n'+json.dumps(rpc('ping')).encode()+b'\n'); out=[json.loads(x) for x in p.stdout.splitlines()]
        self.assertEqual(out[0]['error']['code'],-32700); self.assertEqual(out[1]['result'],{})
    def test_oversized_frame(self):
        p=call(['mcp'],b'x'*262145+b'\n'); self.assertEqual(p.returncode,2)
        self.assertEqual(json.loads(p.stdout)['error']['code'],-32700)
    def test_identifier_limits(self):
        for ident in ('x'*129,9007199254740992):
            p,out=session([rpc('ping',ident)]); self.assertEqual(out[0]['error']['code'],-32600)
    def test_rate_limit(self):
        from unittest.mock import patch
        with patch.object(runtime.time,'monotonic',return_value=0.0):
            server=runtime.Server()
            for msg in initialized(): server.handle(msg)
            req=rpc('tools/call',name=NAME.replace('-','_'),arguments=kernel.SAMPLE)
            for _ in range(20): self.assertFalse(server.handle(req)['result']['isError'])
            limited=server.handle(req)['result']
            self.assertTrue(limited['isError']); self.assertIn('rate limit',limited['content'][0]['text'])


class Validation(unittest.TestCase):
    def test_schema_subset_is_supported(self):
        supported={'$schema','title','description','type','properties','required','additionalProperties','items','minItems','maxItems','uniqueItems','minLength','maxLength','pattern','minimum','maximum','exclusiveMinimum','exclusiveMaximum','enum','default'}
        def walk(s):
            self.assertLessEqual(set(s),supported)
            for x in s.get('properties',{}).values(): walk(x)
            if isinstance(s.get('items'),dict): walk(s['items'])
            if isinstance(s.get('additionalProperties'),dict): walk(s['additionalProperties'])
        walk(kernel.SCHEMA)
    def test_boolean_is_not_number(self):
        with self.assertRaises(ValueError): runtime.check({'type':'number'},True)
    def test_nonfinite(self):
        with self.assertRaises(ValueError): runtime.check({'type':'number'},float('inf'))
    def test_fixture_schema(self):
        runtime.check(kernel.SCHEMA,kernel.SAMPLE)
    def test_static_runtime_imports(self):
        import ast
        for module in (kernel,runtime):
            tree=ast.parse(Path(module.__file__).read_text())
            banned={'socket','subprocess','pickle','marshal','requests','urllib','http','ctypes'}
            for node in ast.walk(tree):
                if isinstance(node,ast.Import): self.assertFalse({x.name.split('.')[0] for x in node.names}&banned)
                if isinstance(node,ast.ImportFrom): self.assertNotIn((node.module or '').split('.')[0],banned)
                if isinstance(node,ast.Call) and isinstance(node.func,ast.Name): self.assertNotIn(node.func.id,{'eval','exec','compile','open'})

if __name__ == '__main__':
    unittest.main()
