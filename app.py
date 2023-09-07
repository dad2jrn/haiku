import os, openai
from typing import Optional, Union
from functools import wraps
from fastapi import FastAPI


app = FastAPI()


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


@app.get("/")
def get_root():
    return {"Hello": "World!"}


@app.get("/haiku")
def get_haiku():
    return {"Hello": "World!"}
