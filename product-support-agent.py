import asyncio
from pathlib import Path
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

async def main():
    model = ChatOpenAI(model="gpt-5-mini")

    async with MCPAdapter(Path(__file__).parent / "product-support-server.py") as adapter:
        tools = await adapter.list_tools()

        # for tool in tools:
        #     print(f"Tool: {tool.name}")

        agent = create_agent(model, tools)

        result = await agent.ainvoke({"messages": [{"role": "user", "content": "I got a package from you but it was damaged. I need to return it."}]})

        for message in result["messages"]:
            message.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())
