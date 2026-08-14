from api_wrapper import LLMAPIWrapper


def main():
    wrapper = LLMAPIWrapper()

    result = wrapper.send_message(
        "Explain machine learning in two simple sentences.",
        temperature=0.3,
    )

    if result["success"]:
        print("Response:")
        print(result["response"])

        print("\nToken Usage:")
        print(f"Input: {result['input_tokens']}")
        print(f"Output: {result['output_tokens']}")
        print(f"Total: {result['total_tokens']}")

    else:
        print("Request failed:")
        print(result["error"])


if __name__ == "__main__":
    main()