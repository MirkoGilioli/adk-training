from google.adk.agents import LlmAgent as Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams


mcp_toolbox = MCPToolset(
    connection_params= StreamableHTTPConnectionParams(
        url="https://ow-mcp-server-921355774260.us-central1.run.app/mcp"
    )
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='You are an helpful assistant. Your goal is to provide weather news',
    instruction='Answer user questions using your tools',
    tools=[
        mcp_toolbox
    ]
)
