from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from turso_client import Turso

# Router setup
router = APIRouter()

# OAuth2 setup for user authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Template rendering setup
templates = Jinja2Templates(directory="templates")

# Turso Database credentials
TURSO_URL = "libsql://dbstart-nabilaprapty.turso.io"
TURSO_TOKEN = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJnaWQiOiI0NTdiNjMzNC05NWM4LTRiZmMtYjJkNS1hMGE3NDQyZjk3MjciLCJpYXQiOjE3Mzc4MTI4NzZ9.fVwe3TZwo3CSi--6RkERu88wiy4PhBnPsQrUsU3kenPOu9t2U1Kp62xdVzSX2vsO--0I2o6rzYT6TRCVe9MgDA"

# Initialize Turso client
client = Turso(TURSO_URL, TURSO_TOKEN)


# Helper function to fetch user data from Turso
def fetch_user_data(email: str):
    try:
        query = "SELECT * FROM users WHERE email = ?;"
        result = client.execute(query, [email])
        if not result:
            return None
        return result[0]
    except Exception as e:
        print(f"Error fetching user data: {e}")
        return None


# Dependency to get the current user
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Decode the token to get the user's email (replace this with actual token decoding logic)
    email = token  # Replace with real logic for decoding token to email

    # Fetch user data from the database
    user = fetch_user_data(email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token or user not found")
    return user


def fetch_user_data(email: str):
    try:
        query = "SELECT * FROM users WHERE email = ?;"
        result = client.execute(query, [email])
        if not result:
            return None
        return result[0]
    except Exception as e:
        print(f"Error fetching user data: {e}")
        return None
    

def add_new_booking(booking_data):
    try:
        query = """
        INSERT INTO bookings (user_id, room_id, check_in, check_out) VALUES (?, ?, ?, ?);
        """
        client.execute(query, [booking_data['user_id'], booking_data['room_id'], booking_data['check_in'], booking_data['check_out']])
        print("Booking added successfully!")
        return {"success": True, "message": "Booking added successfully!"}
    except Exception as e:
        print(f"Error adding booking: {e}")
        return {"success": False, "message": "Failed to add booking."}
