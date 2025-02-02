from fastapi import APIRouter, Form, Request
import os
from authlib.integrations.starlette_client import OAuth, Config
from fastapi.responses import JSONResponse
from app.utils.recaptcha import verify_recaptcha
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/")
async def home():
    return {"message": "Welcome to the app"}
config_data = {
    "GOOGLE_CLIENT_ID":os.getenv("GOOGLE_CLIENT_ID"),
    "GOOGLE_CLIENT_SECRET": os.getenv("GOOGLE_CLIENT_SECRET"),
}

config = Config(environ=config_data)
oauth = OAuth(config)

oauth.register(
    name="google",
    client_id=config_data["GOOGLE_CLIENT_ID"],
    client_secret=config_data["GOOGLE_CLIENT_SECRET"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid profile email"},
    issuer="https://accounts.google.com",  # Add this
)

# PocketBase URL 
POCKETBASE_URL = "http://127.0.0.1:8090/api/"

@router.get("/oauth/google")
async def google_oauth(request: Request):
    redirect_uri = request.url_for("oauth_google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)

router.get("/oauth")
async def oauth_form(request: Request):
    return templates.TemplateResponse("oauth.html", {"request": request})

