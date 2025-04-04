# MCP SBOM Server

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-1.6-CC5500.svg)](https://www.anthropic.com/news/model-context-protocol)

MCP server to perform a Trivy scan and produce an SBOM in CycloneDX format.

### Prerequisites

- [Node.js](https://nodejs.org/en)
- [trivy](https://github.com/aquasecurity/trivy)
- [uv](https://github.com/astral-sh/uv)

## Development

## Building

> [!NOTE]
> This project employs `uv`.

1. Synchronize dependencies and update the lockfile.
```
uv sync
```

## Debugging

Use [MCP Inspector](https://github.com/modelcontextprotocol/inspector).

Launch the MCP Inspector as follows:

```
npx @modelcontextprotocol/inspector uv --directory /path/to/mcp-sbom run mcp-sbom
```

![MCP Inspector](docs/mcp-inspector.png)
