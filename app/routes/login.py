from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import requests

# Router
router = APIRouter()

# Define templates directory
templates = Jinja2Templates(directory="templates")

@router.get("/login", response_class=HTMLResponse)
async def show_login_form(request: Request):
    """Render the login form."""
    return templates.TemplateResponse("login.html", {"request": request})
