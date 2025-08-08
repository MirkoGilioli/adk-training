from google.adk.agents.llm_agent import Agent
from google.adk.code_executors import BuiltInCodeExecutor
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Executes Python code to perform calculations.',
    instruction="""
    You are a calculator agent.
    When given a mathematical expression, write and execute Python code to calculate the result.
    """,
    code_executor=BuiltInCodeExecutor(),
)
