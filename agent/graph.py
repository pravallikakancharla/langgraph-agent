from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from agent.state import State

from tools.calculator import calculator
from tools.date_tool import get_day
from tools.weather import get_weather

load_dotenv()
# -----------------------------
# 1. Create LLM
# -----------------------------

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


# -----------------------------
# 2. Register Tools
# -----------------------------

tools = [
    calculator,
    get_day,
    get_weather
]


# Give tools to the LLM
llm_with_tools = llm.bind_tools(tools)


# -----------------------------
# 3. AI Node
# -----------------------------

def ask_ai(state: State):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# -----------------------------
# 4. Tool Node
# -----------------------------

tool_node = ToolNode(tools)


# -----------------------------
# 5. Decide Next Step
# -----------------------------

def should_continue(state: State):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return END


# -----------------------------
# 6. Build Graph
# -----------------------------

graph_builder = StateGraph(State)


graph_builder.add_node(
    "ask_ai",
    ask_ai
)


graph_builder.add_node(
    "tools",
    tool_node
)


# START → AI

graph_builder.add_edge(
    START,
    "ask_ai"
)


# AI → Tools OR END

graph_builder.add_conditional_edges(
    "ask_ai",
    should_continue,
    {
        "tools": "tools",
        END: END
    }
)


# Tools → AI

graph_builder.add_edge(
    "tools",
    "ask_ai"
)


# Compile

graph = graph_builder.compile()