import os
import time
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError, APIConnectionError, APITimeoutError
from openai import AuthenticationError, RateLimitError


class LLMAPIWrapper:
    """
    Reusable wrapper for making LLM API calls.

    Handles:
    - Sending messages
    - Retries
    - Timeouts
    - Token usage
    - Rate-limit errors
    - Invalid API keys
    - Unexpected API responses
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gemini-3.1-flash-lite",
        timeout: float = 30.0,
        max_retries: int = 3,
    ):
        """
        Initialize the API wrapper.

        Args:
            api_key: API key. If not provided, reads GEMINI_API_KEY.
            model: Model to use.
            timeout: Maximum time to wait for an API response.
            max_retries: Maximum number of retry attempts.
        """

        load_dotenv(r"D:\vaultx-ai-internship\.env")

        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model
        self.timeout = timeout
        self.max_retries = max_retries

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set. "
                "Please add it to your .env file."
            )

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=(
                "https://generativelanguage.googleapis.com/"
                "v1beta/openai/"
            ),
            timeout=self.timeout,
            max_retries=0,
        )

    def send_message(
        self,
        message: str,
        temperature: float = 0.7,
    ) -> dict:
        """
        Send a message to the LLM.

        Returns a dictionary containing:
        - success
        - response
        - input_tokens
        - output_tokens
        - total_tokens
        - error
        """

        if not message or not message.strip():
            return {
                "success": False,
                "response": None,
                "input_tokens": 0,
                "output_tokens": 0,
                "total_tokens": 0,
                "error": "Message cannot be empty.",
            }

        for attempt in range(1, self.max_retries + 1):

            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": message,
                        }
                    ],
                    temperature=temperature,
                )

                # Safely extract response content
                if (
                    not response
                    or not response.choices
                    or not response.choices[0].message
                ):
                    return {
                        "success": False,
                        "response": None,
                        "input_tokens": 0,
                        "output_tokens": 0,
                        "total_tokens": 0,
                        "error": "Invalid or empty response from API.",
                    }

                content = response.choices[0].message.content

                if not content:
                    return {
                        "success": False,
                        "response": None,
                        "input_tokens": 0,
                        "output_tokens": 0,
                        "total_tokens": 0,
                        "error": "API returned an empty response.",
                    }

                # Safely retrieve token usage
                usage = getattr(response, "usage", None)

                input_tokens = getattr(
                    usage,
                    "prompt_tokens",
                    0,
                ) if usage else 0

                output_tokens = getattr(
                    usage,
                    "completion_tokens",
                    0,
                ) if usage else 0

                total_tokens = getattr(
                    usage,
                    "total_tokens",
                    0,
                ) if usage else 0

                return {
                    "success": True,
                    "response": content,
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "total_tokens": total_tokens,
                    "error": None,
                }

            except AuthenticationError:
                return {
                    "success": False,
                    "response": None,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0,
                    "error": (
                        "Authentication failed. "
                        "Please check your API key."
                    ),
                }

            except RateLimitError:
                if attempt < self.max_retries:
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                    continue

                return {
                    "success": False,
                    "response": None,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0,
                    "error": (
                        "Rate limit exceeded after "
                        f"{self.max_retries} attempts."
                    ),
                }

            except APITimeoutError:
                if attempt < self.max_retries:
                    time.sleep(2)
                    continue

                return {
                    "success": False,
                    "response": None,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0,
                    "error": (
                        "API request timed out after "
                        f"{self.max_retries} attempts."
                    ),
                }

            except APIConnectionError:
                if attempt < self.max_retries:
                    time.sleep(2)
                    continue

                return {
                    "success": False,
                    "response": None,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0,
                    "error": (
                        "Could not connect to the API "
                        "after multiple attempts."
                    ),
                }

            except APIError as error:
                if attempt < self.max_retries:
                    time.sleep(2)
                    continue

                return {
                    "success": False,
                    "response": None,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0,
                    "error": f"API error: {error}",
                }

            except Exception as error:
                return {
                    "success": False,
                    "response": None,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0,
                    "error": f"Unexpected error: {error}",
                }

        return {
            "success": False,
            "response": None,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "error": "Request failed after all retry attempts.",
        }