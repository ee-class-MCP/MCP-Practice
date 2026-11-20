# NOTE OF MCP
## What is MCP?
The Model Context Protocol (MCP) lets applications provide context to LLMs in a standardized way, separating the concern of providing context from the LLM interaction itself. --https://py.sdk.modelcontextprotocol.io/
<img width="580" height="326" alt="image" src="https://github.com/user-attachments/assets/10ec111a-fc0e-43e0-8c83-ed550374af17" />
- MCP Host: Your AI chat interface (such as Claude Desktop)
- MCP Client: Handle the communication between the host & server.
- MCP Server: Expose tools & data to Agent.
### Why we need it?
![alt text](image.png)
## Comparison between Skill & MCP
### Skill
Skill is a folder that tells agent how to do a specific work, and provides the SOP.
Below is an example of file structure.
```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```
### MCP
MCP server is a program(such as `weather.py`) that exposes tools and data to agent.
You can define your MCP tools in the program, which can be used by agent.

### Relation between Skill & MCP
| Skill | MCP |
| :--: | :--: |
| A folder teaches an agent how to do specific task, such as SOP, style etc. | MCP server is a program that exposes tools and data to agent. |
|Skill.md + scripts/references/assets | Tool defines with @mcp.tool() |

MCP is tools that agent can use.
To finish a work, agent may use MCP tools accroding to Skill.

## Python MCP SDK

| MCPServer |  @mcp.tool() | @mcp.resource()|
|:-:|:-:|:-:|
| Use the class to create mcp object. Then, we can use mcp object’s methods, such as tool, resource etc.| It’ll return a decorator, and turn your function a tool. | Same as tool(), but turns your function into a resource (read-only data with a URI). |

```py
from mcp.server import MCPServer

mcp = MCPServer("Demo") # Create an mcp object

@mcp.tool() # Register add function as mcp tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.resource("greeting://{name}") # Register greeting function as mcp resource template.
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```
