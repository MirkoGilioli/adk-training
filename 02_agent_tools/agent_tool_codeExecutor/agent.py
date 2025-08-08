import textwrap
from google.adk.agents.llm_agent import Agent
from google.adk.code_executors import BuiltInCodeExecutor

# Define constants for this example agent
AGENT_NAME = "root_agent"
GEMINI_MODEL = "gemini-2.5-flash"

root_agent = Agent(
    model=GEMINI_MODEL,
    name=AGENT_NAME,
    description='Executes Python code to perform calculations.',
    instruction=textwrap.dedent("""\
        You are a calculator agent.
        When given a mathematical expression, write and execute Python code to calculate the result.
        """),
    code_executor=BuiltInCodeExecutor(),
)
