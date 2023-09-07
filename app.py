import os
from openai_logic import ChatGPT
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add middleware for CORS handling
origins = [
    "http://localhost:8000",
    # "https://example.com",
    # add other origins if necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    # return {"Hello": "World!"}


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
    return {"haiku": haiku.strip()}
