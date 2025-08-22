# Import the Agent class from the Google ADK agent library.
from google.adk.agents.llm_agent import Agent

# Import necessary components for working with the BigQuery toolset.
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
# Import the load_dotenv function to load environment variables from a .env file.
from dotenv import load_dotenv

# Load environment variables from the .env file.
load_dotenv()

# Define constants for this example agent
AGENT_NAME = "bigquery"
GEMINI_MODEL = "gemini-2.5-flash"

# Define a tool configuration to block any write operations
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

# Instantiate a BigQuery toolset
bigquery_toolset = BigQueryToolset(
    bigquery_tool_config=tool_config
)

# Define the BigQuery agent.
bigquery_agent = Agent(
    model=GEMINI_MODEL,
    name=AGENT_NAME,
    description=(
 # Provide a clear description of the agent's capabilities.
        "Agent to answer questions about BigQuery data and execute"
        " SQL queries."
    ),
 # Define the instructions for the agent to follow.
    instruction="""\
        You are a data analyst agent with access to several BigQuery tools.
        Make use of those tools to answer the user's questions.
    """,
    tools=[bigquery_toolset],
)

root_agent = bigquery_agent
# Set the root agent for the application to the bigquery_agent.

