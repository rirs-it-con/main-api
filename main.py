from fastapi import FastAPI 
from open_api import custom_openapi
from routers import api_router

app = FastAPI()

def api_documentation():
    return custom_openapi(app=app)


app.include_router(api_router)
app.openapi = api_documentation