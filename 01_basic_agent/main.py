from basic_agent.agent import root_agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import asyncio
from dotenv import load_dotenv

async def call_agent_async(query: str, runner: Runner, user_id: str, session_id: str):
    """Sends a query to the agent and prints the final response."""
    # Create a Content object with the user's query.
    content = types.Content(role='user', parts=[types.Part(text=query)])

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=content
    ):
        if event.is_final_response():
            # If the event is the final response, extract the text.
            final_response_text = event.content.parts[0].text
        elif event.actions and event.actions.escalate:
            final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
        break
    print(f"<<< Agent Response: {final_response_text}")



async def main():
    """Main function to set up and run the agent interaction."""
    # Load environment variables from a .env file.
    load_dotenv()
    
    # Define application, user, and session identifiers.
    APP_NAME="basic_agent_app"
    USER_ID="user01"
    SESSION_ID="session01"
    
    # Initialize an in-memory session service.
    session_service = InMemorySessionService()

    # Create a new session or load an existing one.
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    runner = Runner(
        # Initialize the runner with the agent, session service, and app name.
        agent=root_agent,
        session_service=session_service,
        app_name=APP_NAME
    )
    user_query = input("Enter your query: ")
    # Call the agent asynchronously with the user's query.
    await call_agent_async(
        query=user_query,
        runner=runner,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

if __name__ == "__main__":
    while True: # Keep the session alive to chat with the agent
        print("Type 'exit' to quit.")
        if input() == "exit":
            break
        asyncio.run(main())




