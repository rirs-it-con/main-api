from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import ApplicationForm
from aiohttp import ClientSession
from dotenv import load_dotenv

load_dotenv()

import os
from bot import bot

api_router = APIRouter()

@api_router.get("/api")
def root():
    return JSONResponse({"api_versions": ["v1"]})

@api_router.post("/api/v1/tg_bot_message")
async def tg_bot_msg(appForm):
    print(appForm)