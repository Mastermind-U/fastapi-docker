from fastapi import FastAPI, Depends
from config import get_settings, Settings



def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or Settings()
    app = FastAPI(name="template", debug=settings.DEBUG)
    app.depndency_overrides = {
        get_settings: lambda: settings,
    }
    return app

app = create_app()

@app.get('/')
def hello_world(settings: Settings = Depends(get_settings)):
    return "Hello World!"
