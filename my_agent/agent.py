from google.adk.agents.llm_agent import Agent

def initiate():
    print("Initiating the agent with necessary tools and resources...")
    return None

system_prompt = """
You are root_agent. You have one tool: initiate().

Step 1: Call initiate() at the start of every conversation.
Step 2: After initiate() returns, reply to the user in plain text only.

You only ever make one tool call per conversation: initiate().
After that, respond in plain text. No other tools exist.
"""

root_agent = Agent(
    model="ollama/llama3.2",
    name='root_agent',
    description='A helpful assistant for user questions using the given tools',
    instruction=system_prompt,
    tools=[initiate]
)
