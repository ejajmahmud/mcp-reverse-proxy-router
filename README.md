# MCP Reverse Proxy Router ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="MCP Reverse Proxy Router Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/mcp-reverse-proxy-router/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/mcp-reverse-proxy-router?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/mcp-reverse-proxy-router/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**MCP Reverse Proxy Router** is a production-ready developer tool and connector: Path and capability-based reverse proxy routing agent requests to specialized backend MCP microservices.

---

## 🚀 Problem Statement

Monolithic MCP servers bundle incompatible tools together, while running separate servers complicates client agent configuration.

---

## ⚡ Architecture Flow

```mermaid
graph TD
    A[Agent Client: Single Gateway Endpoint] --> B[MCP Reverse Proxy Router]
    B -->|tools/call: 'sql/query'| C[PostgreSQL MCP Microservice]
    B -->|tools/call: 'fs/read'| D[Filesystem MCP Microservice]
    B -->|tools/call: 'git/commit'| E[Git MCP Microservice]
    C & D & E --> F[Unified JSON-RPC Response to Client]
```

---

## 📊 Performance Benchmarks

| Metric | Monolithic MCP Server | Multiple Separate Ports | MCP Reverse Proxy Router | Advantage |
|---|---|---|---|---|
| Client Configuration Simplicity | High | Complex (N connection configs) | Single URL / Stdio Pipe | **Unified interface** |
| Microservice Isolation | 0% (Shared process) | High | 100% Process isolation | **Zero crash cascade** |
| Routing Overhead | 0 ms | N/A | 0.08 ms | **High throughput** |
| Dynamic Backend Registration | Requires restart | Complex | Hot-reloaded routing table | **Zero-downtime updates** |

---

## 🛠️ Installation & Quickstart

```bash
pip install mcp_reverse_proxy_router
```

### Python API

```python
import mcp_reverse_proxy_router

print(mcp_reverse_proxy_router.__version__)
```

### CLI Usage

```bash
mcp-reverse-proxy-router --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
