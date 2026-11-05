"""CLI for mcp-reverse-proxy-router."""
import sys
import argparse
from .router import ReverseProxyRouter


def main():
    parser = argparse.ArgumentParser(description="MCP Reverse Proxy Router")
    parser.add_argument("--demo", action="store_true", help="Run reverse proxy routing demonstration")
    args = parser.parse_args()

    router = ReverseProxyRouter()
    if args.demo:
        router.register_prefix_route("db_", lambda args: f"Handled by DB Service: {args}")
        router.register_prefix_route("fs_", lambda args: f"Handled by FS Service: {args}")

        print(router.route_call("db_query", {"table": "users"}))
        print(router.route_call("fs_read", {"path": "/etc/hosts"}))
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
