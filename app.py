import os, openai
from typing import Optional, Union
from functools import wraps
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def get_root():
    return {'Hello': 'World!'}

@app.get('/haiku')
def get_haiku():
    pass