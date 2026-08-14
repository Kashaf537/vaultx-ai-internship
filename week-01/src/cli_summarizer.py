import argparse
from api_wrapper import LLMAPIWrapper


def read_file(file_path):
    """Read text from a file safely."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None

    except OSError as error:
        print(f"Error reading file: {error}")
        return None


def generate_analysis(wrapper, text):
    """Generate summary, key points, and sentiment."""

    prompt = f"""
Analyze the following text.

Return your response using exactly this structure:

SUMMARY:
Write a concise summary of the text in 2-3 sentences.

KEY POINTS:
- Point 1
- Point 2
- Point 3

SENTIMENT:
Choose one: Positive, Negative, or Neutral.

TEXT:
{text}
"""

    return wrapper.send_message(
        prompt,
        temperature=0.3
    )


def main():
    parser = argparse.ArgumentParser(
        description=(
            "CLI tool that generates a summary, "
            "key points, and sentiment from text."
        )
    )

    input_group = parser.add_mutually_exclusive_group()

    input_group.add_argument(
        "--text",
        type=str,
        help="Text to analyze directly."
    )

    input_group.add_argument(
        "--file",
        type=str,
        help="Path to a text file to analyze."
    )

    args = parser.parse_args()

    # -----------------------------------------
    # Get input text
    # -----------------------------------------

    if args.text:
        text = args.text

    elif args.file:
        text = read_file(args.file)

        if text is None:
            return

    else:
        # Interactive file input
        print("\nNo input method was provided.")
        print("You can enter the path of a text file to analyze.")

        file_path = input("\nEnter file path: ").strip()

        if not file_path:
            print("Error: No file path provided.")
            return

        text = read_file(file_path)

        if text is None:
            return

    # -----------------------------------------
    # Validate input
    # -----------------------------------------

    if not text.strip():
        print("Error: Input text cannot be empty.")
        return

    # -----------------------------------------
    # Create reusable API wrapper
    # -----------------------------------------

    wrapper = LLMAPIWrapper()

    # -----------------------------------------
    # Generate analysis
    # -----------------------------------------

    result = generate_analysis(wrapper, text)

    if not result["success"]:
        print("\nRequest failed:")
        print(result["error"])
        return

    # -----------------------------------------
    # Display results
    # -----------------------------------------

    print("\n" + "=" * 50)
    print("ANALYSIS")
    print("=" * 50)

    print(result["response"])

    print("\n" + "=" * 50)
    print("TOKEN USAGE")
    print("=" * 50)

    print(f"Input tokens: {result['input_tokens']}")
    print(f"Output tokens: {result['output_tokens']}")
    print(f"Total tokens: {result['total_tokens']}")


if __name__ == "__main__":
    main()