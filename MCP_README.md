# Globalutil MCP for Cursor

This update to globalutil comes with the MCP integration and setup guideline.

## Features

- 📁 Get directory tree structure
- 📖 Get all code for the specific directory with specified extension

## Setup

1. Install the required dependencies:

```bash
conda env create -n globalutil python=3.11
pip install -r requirements_mcp.txt
```

## Usage in Cursor

1. Define the mcp.json inside the ~/.cursor/mcp.json

and it should look something like this:

```
{
    "mcpServers": {
        "directory-structure-server": {
            "command": "/Users/(your username here)/opt/miniconda3/envs/globalutil/bin/python",
            "args": ["/Users/(your username here)/Development/globalutil/mcp/mcp_server.py"],
            "env": {}
        }
    }
}
```

for this creation you don't need to create this file manually you can alternatively go to Cursor/settings/Cursor Settings, on the left tab there should be a tab called MCP (click that), and then click the +add new global mcp server (blue button) at the top right corner of the page opened.

## Important Note on mcp.json:

1. /Users/(your username here)/opt/miniconda3/envs/globalutil/bin/python needs to be the specific python that has the dependencies installed, I use conda you can use any other package manager to ensure that the packages required are installed.

2. /Users/(your username here)/Development/globalutil/mcp/mcp_server.py here is the server definition file, you can either clone this repo, or simply just use this file from the repo to make sure it exists somewhere inside your pc and then you can copy the path to this file (ensure full path not just the name) and replace it inside the mcp.json.
