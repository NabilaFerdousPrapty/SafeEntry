from fastapi import APIRouter, Form, Request
from fastapi.responses import JSONResponse
from app.utils.recaptcha import verify_recaptcha
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
router = APIRouter()

@router.get("/")
async def home():
    return {"message": "Welcome to the app"}

@router.get("/signup")
async def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.post("/signup")
async def signup(username: str = Form(...), email: str = Form(...), g_recaptcha_response: str = Form(...)):
    # Verify Google reCAPTCHA
    is_valid = verify_recaptcha(g_recaptcha_response)
    if not is_valid:
        return JSONResponse(content={"success": False, "message": "Invalid reCAPTCHA"}, status_code=400)

    # Proceed with user registration
    return JSONResponse(content={"success": True, "message": "Signup successful!"})

# Define the path to the templates directory
templates = Jinja2Templates(directory="templates")  # Make sure the templates folder is in the root of your project

@router.get("/signup", response_class=HTMLResponse)
async def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})