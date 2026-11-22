# Core utilities package
import socket

# Resilient DNS fallback for huggingface.co
# On some networks/ISPs (e.g. campus Wi-Fi or regional DNS servers),
# default DNS lookups for huggingface.co may fail with RCODE_SERVER_FAILURE.
# This fallback transparently queries Cloudflare/AWS anycast IPs if system resolution fails.
_orig_getaddrinfo = socket.getaddrinfo
_HF_FALLBACK_IPS = ["99.86.30.112", "99.86.30.85", "99.86.30.118", "99.86.30.69"]

def _resilient_getaddrinfo(host, port, *args, **kwargs):
    try:
        return _orig_getaddrinfo(host, port, *args, **kwargs)
    except socket.gaierror:
        if host == "huggingface.co":
            for ip in _HF_FALLBACK_IPS:
                try:
                    return _orig_getaddrinfo(ip, port, *args, **kwargs)
                except Exception:
                    continue
        raise

socket.getaddrinfo = _resilient_getaddrinfo
