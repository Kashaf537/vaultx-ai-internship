import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv(r"D:\vaultx-ai-internship\.env")

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# Create OpenAI client configured to use Gemini API
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Send a prompt to the model
response = client.chat.completions.create(
    model="gemini-3.1-flash-lite",
    messages=[
        {
            "role": "user",
            "content": "Explain artificial intelligence in two simple sentences."
        }
    ]
)

# Print the model response
print("Response:")
print(response.choices[0].message.content)

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

# Print token usage
print("\nToken Usage:")
print(f"Input tokens: {input_tokens}")
print(f"Output tokens: {output_tokens}")
print(f"Total tokens: {total_tokens}")

# Gemini pricing
# Update these values if you switch to a paid model.
INPUT_PRICE_PER_MILLION = 0.00
OUTPUT_PRICE_PER_MILLION = 0.00

# Calculate cost
input_cost = (input_tokens / 1_000_000) * INPUT_PRICE_PER_MILLION
output_cost = (output_tokens / 1_000_000) * OUTPUT_PRICE_PER_MILLION
total_cost = input_cost + output_cost

# Print cost
# Free-tier pricing for the selected Gemini model
print("\nCost:")
print(f"Input cost: ${input_cost:.8f}")
print(f"Output cost: ${output_cost:.8f}")
print(f"Total cost: ${total_cost:.8f}")