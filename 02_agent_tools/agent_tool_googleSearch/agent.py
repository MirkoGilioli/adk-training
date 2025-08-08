from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

# Define constants for this example agent
AGENT_NAME = "root_agent"
GEMINI_MODEL = "gemini-2.5-flash"

root_agent = Agent(
    model=GEMINI_MODEL,
    name=AGENT_NAME,
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[
        google_search
    ]
)
