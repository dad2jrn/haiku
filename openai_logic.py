import openai
from typing import Optional
from functools import wraps


def handle_openai_errors(func) -> Optional[str]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        A decorator to handle OpenAI API errors gracefully.

        This decorator wraps a function that makes OpenAI API calls, catching
        any OpenAIError exceptions and returning their string representation.

        Args:
            func (callable): The function to be wrapped.

        Returns:
            Optional[str]: The string representation of an OpenAIError, if one occurs,
                        or None if the function succeeds without raising an exception.
        """
        try:
            return func(*args, **kwargs)
        except openai.error.OpenAIError as e:
            return str(e)

    return wrapper

class ChatGPT:
    """Generates a chatbot using the OpenAI GPT-3.5 Turbo model.
    """
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        openai.api_key = self.api_key

    @