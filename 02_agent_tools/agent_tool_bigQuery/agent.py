from google.adk.agents.llm_agent import Agent

from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from dotenv import load_dotenv

load_dotenv()

# Define constants for this example agent
AGENT_NAME = "bigquery"
APP_NAME = "bigquery_app"
GEMINI_MODEL = "gemini-2.5-flash"

# Define a tool configuration to block any write operations
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

# Instantiate a BigQuery toolset
bigquery_toolset = BigQueryToolset(
    bigquery_tool_config=tool_config
)

# Agent Definition
bigquery_agent = Agent(
    model=GEMINI_MODEL,
    name=AGENT_NAME,
    description=(
        "Agent to answer questions about BigQuery data and execute"
        " SQL queries."
    ),
    instruction="""\
        You are a data analyst agent with access to several BigQuery tools.
        Make use of those tools to answer the user's questions.
    """,
    tools=[bigquery_toolset],
)

root_agent = bigquery_agent

