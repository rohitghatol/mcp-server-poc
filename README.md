# Overview

MCP Server for File System

This project uses the [uv](https://github.com/astral-sh/uv) package manager.
The initial dependency is `fastmcp`. For setup and server details see
<https://gofastmcp.com/servers/fastmcp>.

## Authorship

This repository and the accompanying code were generated with the help of
OpenAI Codex.

## MCP Tools

The server provides basic commands to control the file system:

- List directory contents
- Create directories
- Remove directories
- Create files
- Delete files

## Usage

Run the server with:

```bash
python main.py
```

Once running, type commands at the `mcp>` prompt:

```
ls [path]        list contents of a directory
mkdir <path>     create a directory
rmdir <path>     remove a directory
touch <path>     create an empty file
rm <path>        delete a file
help             show available commands
exit             quit the server
```

This server executes commands directly and does not watch for file system
changes.
