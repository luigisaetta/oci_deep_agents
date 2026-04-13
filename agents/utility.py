"""Utility functions for Deep Agents examples."""


def extract_text_from_content(content: object) -> str:
    """Extract displayable text from model content payload."""
    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):
        chunks = []
        for item in content:
            if isinstance(item, str):
                chunks.append(item)
                continue
            if isinstance(item, dict):
                if isinstance(item.get("text"), str):
                    chunks.append(item["text"])
                    continue
                if isinstance(item.get("content"), str):
                    chunks.append(item["content"])
                    continue
        return "\n".join(chunk.strip() for chunk in chunks if chunk and chunk.strip())

    if isinstance(content, dict):
        if isinstance(content.get("text"), str):
            return content["text"].strip()
        if isinstance(content.get("content"), str):
            return content["content"].strip()

    return ""


def extract_response_text(result: object) -> str:
    """Extract assistant text from deep agent result."""
    if isinstance(result, dict):
        messages = result.get("messages", [])
        if isinstance(messages, list) and messages:
            last_message = messages[-1]

            content = getattr(last_message, "content", None)
            if content is None and isinstance(last_message, dict):
                content = last_message.get("content")

            text = extract_text_from_content(content)
            if text:
                return text

    return str(result)


def extract_token_usage(result: object) -> dict[str, int]:
    """Extract token usage from the last assistant message metadata."""
    token_usage: dict[str, int] = {}

    if not isinstance(result, dict):
        return token_usage

    messages = result.get("messages", [])
    if not isinstance(messages, list) or not messages:
        return token_usage

    last_message = messages[-1]
    usage = getattr(last_message, "usage_metadata", None)
    response_metadata = getattr(last_message, "response_metadata", None)

    if usage is None and isinstance(last_message, dict):
        usage = last_message.get("usage_metadata")
    if response_metadata is None and isinstance(last_message, dict):
        response_metadata = last_message.get("response_metadata")

    if isinstance(usage, dict):
        for key in ("input_tokens", "output_tokens", "total_tokens"):
            value = usage.get(key)
            if isinstance(value, int):
                token_usage[key] = value

    if isinstance(response_metadata, dict):
        response_token_usage = response_metadata.get("token_usage")
        if isinstance(response_token_usage, dict):
            mapping = {
                "prompt_tokens": "input_tokens",
                "completion_tokens": "output_tokens",
                "total_tokens": "total_tokens",
            }
            for source_key, target_key in mapping.items():
                value = response_token_usage.get(source_key)
                if isinstance(value, int) and target_key not in token_usage:
                    token_usage[target_key] = value

    return token_usage


def print_result(
    question: str, response_text: str, token_usage: dict[str, int]
) -> None:
    """Print result in a clean visual layout."""
    print("\n" + "=" * 72)
    print("DEEP AGENT RESULT")
    print("=" * 72)
    print(f"Question: {question}\n")
    print("Response Text")
    print("-" * 72)
    print(response_text or "(No response text extracted)")
    print("-" * 72)

    print("Token Usage")
    print("-" * 72)
    if not token_usage:
        print("No token usage metadata found in the response.")
    else:
        print(f"{'Metric':<20} {'Value':>10}")
        print(f"{'input_tokens':<20} {token_usage.get('input_tokens', 0):>10}")
        print(f"{'output_tokens':<20} {token_usage.get('output_tokens', 0):>10}")
        print(f"{'total_tokens':<20} {token_usage.get('total_tokens', 0):>10}")
    print("=" * 72 + "\n")
