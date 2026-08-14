import os
import csv
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(r"D:\vaultx-ai-internship\.env")

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# Create OpenAI client configured for Gemini
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Same prompt for every experiment
prompt = (
    "Write a short description of a rainy evening in a busy city. "
    "Describe the atmosphere, surroundings, and emotions in 80–100 words."
)

# Temperatures required by the internship
temperatures = [0, 0.7, 1.0]

# Store all experiment results
results = []

# Run the same prompt 3 times at each temperature
for temperature in temperatures:

    print(f"\n{'=' * 60}")
    print(f"Temperature: {temperature}")
    print(f"{'=' * 60}")

    for run in range(1, 4):

        print(f"\nRun {run}:")

        response = client.chat.completions.create(
            model="gemini-3.1-flash-lite",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=temperature
        )

        output = response.choices[0].message.content

        print(output)

        # Save result
        results.append({
            "temperature": temperature,
            "run": run,
            "output": output
        })


# Save results to CSV
output_file = r"D:\vaultx-ai-internship\week-01\experiments\temperature_results.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["temperature", "run", "output"]
    )

    writer.writeheader()
    writer.writerows(results)

print("\n" + "=" * 60)
print("Experiment completed successfully.")
print(f"Results saved to: {output_file}")
print("=" * 60)