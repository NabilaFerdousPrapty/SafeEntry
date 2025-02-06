from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import requests

# Router
router = APIRouter()

# Define templates directory
templates = Jinja2Templates(directory="templates")


# Verify Google reCAPTCHA
def verify_recaptcha(token: str) -> bool:
    secret_key = ""  # Replace with your reCAPTCHA secret key
    response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={"secret": secret_key, "response": token},
    )
    result = response.json()
    return result.get("success", False)


# Routes
@router.get("/signup", response_class=HTMLResponse)
async def show_signup_form(request: Request):
    """Render the signup form."""
    return templates.TemplateResponse("signup.html", {"request": request})


@router.post("/signup", response_class=HTMLResponse)
async def signup(
    email: str = Form(...),
    password: str = Form(...),
    g_recaptcha_response: str = Form(...),
):
    """Handle signup with Google reCAPTCHA validation."""
    if not verify_recaptcha(g_recaptcha_response):
        return "<div id='response'>Invalid reCAPTCHA. Please try again.</div>"

    # Simulate successful signup
    return "<div id='response'>Signup successful! Welcome aboard.</div>"


@router.get("/login", response_class=HTMLResponse)
async def show_login_form(request: Request):
    """Render the login form."""
    return templates.TemplateResponse("login.html", {"request": request})
 

@router.get('/dashboard', response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@router.get('/profile', response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})



