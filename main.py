from agent.graph import graph
import logging


logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_agent(messages):
    result = graph.invoke({
        "messages": messages
    })

    return result["messages"][-1]


if __name__ == "__main__":
    print("AI Agent is running.")
    print("Type 'exit' to stop.\n")

    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            logging.info("Agent session ended.")
            print("Goodbye!")
            break

        messages.append(("user", user_input))

        try:
            logging.info("User input: %s", user_input)

            response = run_agent(messages)

            print("Agent:", response.content)

            logging.info("Agent response: %s", response.content)

            messages.append(response)

        except Exception as e:
            logging.error("Agent error: %s", e)
            print("Agent error:", e)