# Overview

MCP Server for File System

This project uses the [uv](https://github.com/astral-sh/uv) package manager.
The initial dependency is `fastmcp`. For setup and server details see
<https://gofastmcp.com/servers/fastmcp>.

## Authorship

This repository was created by OpenAI Codex.

## MCP Tools

The server exposes a few basic file-system commands:

- **Listing directories** with `ls [path]`
- **Creating directories** with `mkdir <path>`
- **Deleting directories** with `rmdir <path>`
- **Creating files** with `create <path>`
- **Deleting files** with `delete <path>`

## Running

Install dependencies with uv and start the server:

```bash
uv pip install -r pyproject.toml
python main.py
```
