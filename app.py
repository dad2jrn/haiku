import os
from openai_logic import ChatGPT
from fastapi import FastAPI, HTTPException, Depends


app = FastAPI()





@app.get("/")
def get_root():
    return {"Hello": "World!"}


@app.get("/haiku")
def get_haiku():
    return {"Hello": "World!"}
