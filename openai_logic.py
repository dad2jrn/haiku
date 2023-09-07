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
    """
    Generate a haiku using GPT-3.5 Turbo
    """
    def __init__(self, api_key: str) -> None:
        """
        Initialize with the API key

        Args:
            api_key (str): OpenAI API Key for GPT-3.5 Turbo
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    @handle_openai_errors
    def generate(self, messages) -> Optional[str]:
        """Generates a chatbot response.

        Args:
            messages (List[str]): The messages to be sent to the chatbot.

        Returns:
            Optional[str]: The string representation of an OpenAIError, if one occurs,
                        or None if the function succeeds without raising an exception.
        """
        # Make the API call to generate the haiku
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Extract and return the haiku from the API response
        haiku = response['choices'][0]['message']['content']
        return haiku.strip()