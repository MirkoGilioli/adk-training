from google.adk.agents import LlmAgent as Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

news_agent = Agent(
    name="NewsAgent",
    model="gemini-2.5-flash",
    description="You are a news Agent and your goal is to search for accurate News.",
    instruction="""
        Follow these instructions while searching for news.
        1. Search for latest News
        2. Evaluate if the news is not fake
        3. Provide a summary of the news
    """,
    tools=[
        google_search
    ]
)

weather_agent = Agent(
    name="WeatherAgent",
    model="gemini-2.5-flash",
    description="You are a weather Agent and your goal is to search for latest weather.",
    instruction="""
        Follow these instructions while searching for weather information.
        1. Ask for location if not provided
        2. Search for weather location using your available tools
        3. Provide a quick summary of the weather information, including temperature, humidity, and wind speed.
    """,
    tools=[
        google_search
    ]
)

root_agent = Agent(
    name="HelpDesk",
    model="gemini-2.5-flash",
    description="You are a helpful assistant for user questions.",
    instruction="""
        Follow these instructions to answer user questions.
        1. Use the `NewsAgent` if the user is looking for the latest news
        2. Use the `WeatherAgent` if the user is looking for the latest weather
        3. For any other questions, do not provide any information. Just say that you can provide News and Weather information.
    """,
    tools=[
        AgentTool(agent=news_agent),
        AgentTool(agent=weather_agent)
    ]
)