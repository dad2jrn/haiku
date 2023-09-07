import os
from openai_logic import ChatGPT
from fastapi import FastAPI, HTTPException, Depends


app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "World!"}


@app.get("/haiku", response_model=dict)
def get_haiku():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that generates haikus.",
        },
        {
            "role": "user",
            "content": "Generate a haiku for me."
        },
    ]
    api_key = os.environ.get("api_key")
    haiku_generator = ChatGPT(api_key)
    haiku = haiku_generator.generate(messages)

    # return as json and strip newline chars
    return {"haiku": haiku.strip().replace("\n", " ")}
