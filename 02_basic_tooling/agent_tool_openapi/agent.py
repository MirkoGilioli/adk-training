from google.adk.agents import LlmAgent as Agent
from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset
import json

with open("./agent_tool_openapi/event.json") as f:
    openapi_spec_string = f.read()

pet_store_toolset = OpenAPIToolset(spec_str=openapi_spec_string, spec_str_type="json")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Manages a Booking Event Website using tools generated from an OpenAPI spec.",
    instruction="""You are a Booking Event Website assistant managing Events via an API.
    Use the available tools to fulfill user requests.
    When creating an Event, confirm the details echoed back by the API.
    When listing Events, format the output as a table.
    When deleteing an Event, always ask for confirmation.
    """,
    tools=[
        pet_store_toolset
    ]
)
