from langchain_core.tools import tool


@tool
def calculator(a: float, b: float, operation: str) -> str:
    """Perform basic arithmetic using two numbers."""

    if operation == "add":
        return str(a + b)

    if operation == "subtract":
        return str(a - b)

    if operation == "multiply":
        return str(a * b)

    if operation == "divide":
        if b == 0:
            return "Cannot divide by zero."

        return str(a / b)

    return "Unknown operation."