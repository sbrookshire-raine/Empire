"""URL broker — SSRF / redirect guards for EMPIRE's public-web arms.

Centralizes host validation before any outbound fetch: blocks loopback,
RFC1918 private ranges, link-local, and reserved/multicast addresses; also
re-validates the host after redirects (the `final_url` must be safe too).

Used by web_scout / github_scout (and any future public-web arm) so an
attacker-supplied URL can never reach localhost, the LAN, or cloud metadata.

Offline-convertible: pure stdlib (socket + ipaddress).
"""

from __future__ import annotations

import ipaddress
import socket
from urllib.parse import urlparse

ALLOWED_SCHEMES: frozenset[str] = frozenset({"http", "https"})

# Hosts that resolve to the loopback interface must never be fetched.
_BLOCKED_HOSTNAMES: frozenset[str] = frozenset(
    {"localhost", "localhost.localdomain", "ip6-localhost", "metadata.google.internal"}
)


def _is_public_ip(ip: ipaddress.IPv4Address | ipaddress.IPv6Address) -> bool:
    if ip.is_loopback or ip.is_private or ip.is_link_local or ip.is_reserved:
        return False
    if ip.is_multicast or ip.is_unspecified:
        return False
    # Reject IPv4-mapped IPv6 loopback (::ffff:127.0.0.1) explicitly.
    if isinstance(ip, ipaddress.IPv6Address) and ip.ipv4_mapped is not None:
        return _is_public_ip(ip.ipv4_mapped)
    return True


def _hostname_blocked(host: str) -> bool:
    return host.lower().rstrip(".") in _BLOCKED_HOSTNAMES


def resolve_host(host: str) -> list[str]:
    """Resolve a hostname to its addresses (empty on failure)."""
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return []
    addrs: list[str] = []
    for info in infos:
        ip = info[4][0]
        if ip not in addrs:
            addrs.append(ip)
    return addrs


def validate_url(url: str) -> dict[str, Any]:
    """Return {ok: True, normalized} or {ok: False, error}. No network here."""
    cleaned = (url or "").strip().strip("<>").strip().strip("'\"")
    if not cleaned:
        return {"ok": False, "error": "url is required"}

    # Handle markdown link syntax accidentally pasted in.
    if cleaned.startswith("[") and "](" in cleaned:
        import re

        m = re.search(r"\]\((https?://[^)\s]+)\)", cleaned)
        if m:
            cleaned = m.group(1)

    if "://" not in cleaned and not cleaned.startswith(("http:", "https:")):
        # Bare domain → assume https.
        cleaned = "https://" + cleaned.lstrip("/")

    try:
        parsed = urlparse(cleaned)
    except ValueError:
        return {"ok": False, "error": "unparseable URL", "url": cleaned}

    if parsed.scheme not in ALLOWED_SCHEMES:
        return {"ok": False, "error": "only http(s) allowed", "url": cleaned}
    if not parsed.hostname:
        return {"ok": False, "error": "no hostname", "url": cleaned}

    host = parsed.hostname
    if _hostname_blocked(host):
        return {"ok": False, "error": f"blocked host: {host}", "url": cleaned}

    # If host is a literal IP, validate directly.
    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        literal = None
    if literal is not None:
        if not _is_public_ip(literal):
            return {"ok": False, "error": f"blocked address: {host}", "url": cleaned}
        return {"ok": True, "normalized": cleaned, "host": host}

    # Hostname: resolve and require every address to be public (DNS-rebinding guard).
    addrs = resolve_host(host)
    if not addrs:
        return {"ok": False, "error": f"could not resolve host: {host}", "url": cleaned}
    for addr in addrs:
        try:
            ip = ipaddress.ip_address(addr.split("%")[0])
        except ValueError:
            continue
        if not _is_public_ip(ip):
            return {
                "ok": False,
                "error": f"blocked address for {host}: {addr}",
                "url": cleaned,
            }
    return {"ok": True, "normalized": cleaned, "host": host}


def validate_final_url(final_url: str) -> dict[str, Any]:
    """Re-validate the post-redirect URL (a redirect must not land on private IP)."""
    result = validate_url(final_url)
    if not result.get("ok"):
        result["error"] = f"redirect target unsafe: {result.get('error')}"
    return result


def is_public_url(url: str) -> bool:
    return bool(validate_url(url).get("ok"))


def main(argv: list[str] | None = None) -> int:
    import argparse
    import json
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="EMPIRE URL broker (SSRF guard)")
    parser.add_argument("url")
    args = parser.parse_args(argv)
    result = validate_url(args.url)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
