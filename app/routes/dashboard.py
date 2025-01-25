from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer

# Define OAuth2 dependency for user authentication (can be modified as per your auth system)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Router setup
router = APIRouter()

# Template rendering setup
templates = Jinja2Templates(directory="templates")

# Fake user data (replace with database queries)
FAKE_USER_DB = {
    "john_doe": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "role": "Admin",
        "tasks": ["Complete report", "Review PR", "Team meeting"],
    },
    "jane_smith": {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "role": "User",
        "tasks": ["Write blog post", "Update portfolio"],
    },
}


# Dependency to get the current user (example)
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Simulate token-based user extraction (replace with actual validation)
    user_id = token  # Replace this with real token decoding logic
    user = FAKE_USER_DB.get(user_id)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token or user not found")
    return user


# Dashboard route
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, current_user: dict = Depends(get_current_user)):
    """Display the dashboard with user-specific data."""
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": current_user,
            "tasks": current_user.get("tasks", []),
        },
    )

