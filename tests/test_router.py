"""Tests for mcp-reverse-proxy-router."""
import unittest
from mcp_reverse_proxy_router.router import ReverseProxyRouter


class TestReverseProxyRouter(unittest.TestCase):
    def setUp(self):
        self.router = ReverseProxyRouter()

    def test_routing(self):
        self.router.register_exact_route("ping", lambda args: "pong")
        self.router.register_prefix_route("cloud_", lambda args: f"cloud: {args.get('res')}")

        self.assertEqual(self.router.route_call("ping", {}), "pong")
        self.assertEqual(self.router.route_call("cloud_bucket", {"res": "s3"}), "cloud: s3")

    def test_missing_route(self):
        with self.assertRaises(KeyError):
            self.router.route_call("unknown", {})


if __name__ == "__main__":
    unittest.main()
