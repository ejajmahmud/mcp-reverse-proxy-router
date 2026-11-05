"""Reverse proxy router mapping tool names and prefixes to backends."""
from typing import Dict, Any, Callable, Optional


class ReverseProxyRouter:
    def __init__(self):
        self._routes: Dict[str, Callable[[Dict[str, Any]], Any]] = {}
        self._prefix_routes: Dict[str, Callable[[Dict[str, Any]], Any]] = {}

    def register_exact_route(self, tool_name: str, handler: Callable[[Dict[str, Any]], Any]):
        self._routes[tool_name] = handler

    def register_prefix_route(self, prefix: str, handler: Callable[[Dict[str, Any]], Any]):
        self._prefix_routes[prefix] = handler

    def route_call(self, tool_name: str, args: Dict[str, Any]) -> Any:
        if tool_name in self._routes:
            return self._routes[tool_name](args)

        for prefix, handler in self._prefix_routes.items():
            if tool_name.startswith(prefix):
                return handler(args)

        raise KeyError(f"No backend route found for tool: '{tool_name}'")
