from api_wrapper import LLMAPIWrapper


def test_empty_message():
    """Test that an empty message is handled without crashing."""

    wrapper = LLMAPIWrapper()

    result = wrapper.send_message("")

    print("\n--- Empty Message Test ---")
    print("Success:", result["success"])
    print("Error:", result["error"])


def test_invalid_api_key():
    """Test that an invalid API key is handled properly."""

    wrapper = LLMAPIWrapper(
        api_key="invalid-api-key-for-testing"
    )

    result = wrapper.send_message(
        "Explain artificial intelligence in one sentence."
    )

    print("\n--- Invalid API Key Test ---")
    print("Success:", result["success"])
    print("Error:", result["error"])


def test_timeout():
    """Test timeout and retry handling."""

    wrapper = LLMAPIWrapper(
        timeout=0.001,
        max_retries=3
    )

    result = wrapper.send_message(
        "Explain machine learning in one sentence."
    )

    print("\n--- Timeout / Retry Test ---")
    print("Success:", result["success"])
    print("Error:", result["error"])


if __name__ == "__main__":
    test_empty_message()
    test_invalid_api_key()
    test_timeout()