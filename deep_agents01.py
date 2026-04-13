"""
First Deep Agent on OCI Enterprise AI
"""

from deepagents import create_deep_agent
from utility import (
    build_llm_from_env,
    extract_response_text,
    extract_token_usage,
    print_result,
)

llm = build_llm_from_env()

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
