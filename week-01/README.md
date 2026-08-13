# Week 01

## Task 03 — First API Call

For this task, I made my first LLM API call using the OpenAI Python SDK with Google's Gemini API through its OpenAI-compatible API endpoint.

### API Setup

- **SDK:** OpenAI Python SDK
- **API:** Google Gemini API
- **Model:** Gemini 3.1 Flash-Lite
- **Environment variables:** Managed using `python-dotenv`
- **API key:** Stored securely in `.env`

### How It Works

The Python script loads the Gemini API key from the `.env` file and uses the OpenAI SDK to send a prompt to the Gemini API.

```text
Python Script
     ↓
python-dotenv
     ↓
Gemini API Key
     ↓
OpenAI SDK
     ↓
Gemini OpenAI-Compatible API
     ↓
Gemini Model
     ↓
Response