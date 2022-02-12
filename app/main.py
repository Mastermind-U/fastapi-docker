from fastapi import FastAPI
from config import get_settings

settings = get_settings()

app = FastAPI(name="template", debug=settings.DEBUG)


@app.get('/')
def hello_world():
    return "Hello World!"
