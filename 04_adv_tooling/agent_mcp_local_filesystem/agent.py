#The first time we need to install the mcpserver locally with
# npm i @modelcontextprotocol/server-filesystem

from google.adk.agents import LlmAgent as Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, StdioConnectionParams
import os

ABS_TARGET_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'mcp_target/')

mcp_filesystem_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                ABS_TARGET_FOLDER_PATH
            ]
        ),
        timeout=15 # Increase timeout if needed
    )
)


root_agent = Agent(
    model='gemini-2.5-flash',
    name='filesystem_assistant_agent',
    description='A helpful assistant for filesystem questions.',
    instruction='Help the user manage their files. You can list files, read files, etc.',
    tools=[
        mcp_filesystem_toolset
    ]
)
