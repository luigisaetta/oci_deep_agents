"""
Test01: Test the connection to OCI OpenAI and generate a response from the model.
"""

from utility import build_llm_from_env

llm = build_llm_from_env()


def main() -> None:
    """Run a simple question against the configured model."""
    question = "Tell me something about Rome, Italy"
    response = llm.invoke(question)

    print("Question: ", question)
    print("")
    print("Response:")
    print(response.content[0]["text"])
    print("")


if __name__ == "__main__":
    main()
