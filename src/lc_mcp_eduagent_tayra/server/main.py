# SPDX-FileCopyrightText: 2026 Tayra Sakurai
# SPDX-License-Identifier: AGPL-3.0-or-later
from mcp.server.fastmcp import FastMCP
from .chemistry import *

fastMCP = FastMCP("LC-MCP-eduagent-tayra-sv")

if __name__ == '__main__':
    fastMCP.run()
