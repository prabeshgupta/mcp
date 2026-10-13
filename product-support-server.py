from fastmcp import FastMCP

mcp = FastMCP("Product Support Server")

FAQ = {
    "shipping": "We offer free shipping on all orders over $50. Orders are processed within 2-3 business days.",
    "returns": "You can return any item within 7 days of purchase for a full refund. Please ensure the item is in its original condition.",
    "warranty": "All our products come with a 1-year warranty. If you encounter any issues, please contact our support team for assistance.",    
}

ORDERS = {
    "ORD1001":"Your order has been shipped and is expected to arrive within 2 business days.",
    "ORD1002":"Your order is being processed and will be shipped within 3 business days.",
    "ORD1003":"Your order has been delivered. We hope you enjoy your purchase!",
}

@mcp.tool
def search_product_faq(query: str) -> str:
    query = query.lower()
    for keyword, answer in FAQ.items():
        if keyword in query:
            return answer
    return "I'm sorry, I couldn't find any information related to your query. Please contact our support team for further assistance."

@mcp.tool
def check_order_status(order_id: str) -> str:
   return ORDERS.get(order_id.strip().upper(), "I'm sorry, I couldn't find any information related to your order ID. Please contact our support team for further assistance.")

if __name__ == "__main__":
    mcp.run()