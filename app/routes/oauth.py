from fastapi import APIRouter, Form, Request
from fastapi.responses import JSONResponse
from app.utils.recaptcha import verify_recaptcha
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
router = APIRouter()

@router.get("/")
async def home():
    return {"message": "Welcome to the app"}

router.get("/oauth")
async def oauth_form(request: Request):
    return templates.TemplateResponse("oauth.html", {"request": request})

