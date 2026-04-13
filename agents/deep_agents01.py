"""
First Deep Agent on OCI Enterprise AI
"""

import os

from dotenv import load_dotenv
from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI
from .utility import extract_response_text, extract_token_usage, print_result

load_dotenv()

OCI_API_KEY = os.getenv("OCI_API_KEY")
OCI_BASE_URL = os.getenv("OCI_BASE_URL")
MODEL_ID = os.getenv("OCI_MODEL_NAME")
PROJECT_ID = os.getenv("OCI_PROJECT_ID")

default_headers = {"OpenAI-Project": PROJECT_ID}

llm = ChatOpenAI(
    model=MODEL_ID,
    openai_api_base=OCI_BASE_URL,
    openai_api_key=OCI_API_KEY,
    temperature=0.0,
    # important: force responses API (not completions)
    use_responses_api=True,
    output_version="responses/v1",
    # add project id to the request
    default_headers=default_headers,
)

agent = create_deep_agent(
    model=llm,
    system_prompt="You are a research assistant.",
)


def main() -> None:
    """Invoke deep agent and print formatted response plus token stats."""
    question = "Tell me everything you know about Rome, Italy"
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})

    response_text = extract_response_text(result)
    token_usage = extract_token_usage(result)
    print_result(question, response_text, token_usage)


if __name__ == "__main__":
    main()
