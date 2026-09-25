# LangGraph Tool-Using AI Agent

A conversational AI agent built with LangGraph and Groq that can reason about user requests, select appropriate tools, execute them, and return responses.

## Features

- Conversational AI agent using LangGraph
- Groq-powered language model
- Tool calling with LangGraph
- Calculator tool for basic arithmetic
- Date tool for finding the day of the week
- Weather tool using the Open-Meteo API
- Conversation memory during a session
- Error handling for external API failures
- Logging of user inputs and agent responses
- Automated tests using pytest

## Tech Stack

- Python 3.12
- LangGraph
- LangChain
- Groq
- Open-Meteo API
- Requests
- Pytest

## Project Structure

LangGraphAgent/
│
├── agent/
│   ├── __init__.py
│   ├── graph.py
│   └── state.py
│
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   ├── date_tool.py
│   └── weather.py
│
├── tests/
│   └── test_agent.py
│
├── logs/
│
├── main.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

# How It Works

The agent uses a LangGraph workflow to process user messages.

User
  │
  ▼
AI Agent
  │
  ├── Calculator Tool
  │
  ├── Date Tool
  │
  └── Weather Tool
  │
  ▼
Tool Result
  │
  ▼
AI Agent
  │
  ▼
Response

The language model determines when a tool is required. LangGraph manages the workflow between the AI model and the tool execution node.

# Installation

Clone the repository:

git clone https://github.com/pravallikakancharla/langgraph-agent.git
cd langgraph-agent

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

# Install dependencies:

pip install -r requirements.txt
Environment Configuration

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key

The .env file is excluded from Git using .gitignore.

Run the Agent

# Start the application:

python main.py

Example:

AI Agent is running.
Type 'exit' to stop.

You: What is 125 multiplied by 8?
Agent: 1000

You: What day was 2026-09-21?
Agent: Monday

The agent also supports weather queries using latitude and longitude.

# Running Tests

Run the automated test suite:

pytest

Current test coverage includes:

Addition
Multiplication
Division-by-zero handling
Date calculation
Invalid date handling

Example:

5 passed
# Error Handling

The weather tool handles:

Network request failures
HTTP errors
Unexpected API response formats

The application also logs user interactions and errors for debugging.

# Future Improvements

Possible future improvements include:

Persistent conversation memory
Additional external tools and APIs
Voice-agent integration
More comprehensive test coverage
Web-based user interface
Agent observability and tracing
