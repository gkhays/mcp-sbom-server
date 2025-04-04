# MCP SBOM Server

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
cd src/mcp_sbom
npx @modelcontextprotocol/inspector uv --directory /path/to/mcp-sbom run mcp-sbom
```

![MCP Inspector](docs/mcp-inspector.png)
