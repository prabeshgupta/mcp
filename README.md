# Product Support MCP Demo

This project is a simple product support assistant built with Python.
It has:
- a FastMCP server with product FAQ and order lookup tools
- an agent that uses those tools to answer customer support questions

## Files

- `product-support-server.py` — MCP server exposing tools
- `product-support-agent.py` — example agent that connects to the server

## Setup

1. Open a terminal in this project folder.
2. Create a virtual environment
3. Install the required packages:

```bash
pip install fastmcp langchain langchain-openai python-dotenv
```

4. Create a `.env` file and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Run the server

```bash
python product-support-server.py
```

## Run the agent

```bash
python product-support-agent.py
```

The agent will ask about a damaged package and use the product support tools to respond.

## Example tools

- `search_product_faq(query)`
- `check_order_status(order_id)`

These help answer questions about shipping, returns, warranty, and order status.

## Notes

This is a lightweight demo for learning how to connect a model to tools through MCP.
