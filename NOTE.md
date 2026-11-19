# NOTE OF MCP
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
MCP is tools that agent can use.
To finish a work, agent may use MCP tools accroding to Skill.

## Dig into MCP
