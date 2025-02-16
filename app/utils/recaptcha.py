import requests


# Function to verify reCAPTCHA token
def verify_recaptcha(token):
    secret_key = '6Le2RboqAAAAAPEvG8lZgOsNstsk3TX38AIAw5SL'  
    payload = {
        'secret': secret_key,
        'response': token
    }

    # Send a POST request to Google reCAPTCHA API to verify the token
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()

    # Log the response for debugging
    print("reCAPTCHA Response:", result)

    # Check if the response indicates success
    if result.get('success'):
        print("reCAPTCHA verification succeeded")
        return True
    else:
        print("Error: Invalid reCAPTCHA")
        return False

# Function to save user information to Turso
def save_user_to_turso(user_data):
    # Turso Database credentials
    turso_url = "YOUR_TURSO_DATABASE_URL"
    turso_token = "YOUR_TURSO_ACCESS_TOKEN"

    # Initialize Turso client
    client = Turso(turso_url, turso_token)

    # Hash the PIN before storing it in the database
    hashed_pin = hashpw(user_data['pin'].encode(), gensalt()).decode()

    # Insert user data into Turso table
    try:
        query = """
        INSERT INTO users (name, email, mobile, pin) VALUES (?, ?, ?, ?);
        """
        client.execute(query, [user_data['name'], user_data['email'], user_data['mobile'], hashed_pin])
        print("User information saved successfully!")
        return {"success": True, "message": "User information saved successfully!"}
    except Exception as e:
        print(f"Error saving user to Turso: {e}")
        return {"success": False, "message": "Failed to save user information."}

# Function to login user
def login_user(email, pin):
    # Turso Database credentials
    turso_url = "YOUR_TURSO_DATABASE_URL"
    turso_token = "YOUR_TURSO_ACCESS_TOKEN"

    # Initialize Turso client
    client = Turso(turso_url, turso_token)

    try:
        # Query user data by email
        query = "SELECT pin FROM users WHERE email = ?;"
        result = client.execute(query, [email])

        if not result:
            return {"success": False, "message": "Email not found."}

        # Verify the provided PIN against the stored hashed PIN
        stored_hashed_pin = result[0]['pin']
        if checkpw(pin.encode(), stored_hashed_pin.encode()):
            return {"success": True, "message": "Login successful!"}
        else:
            return {"success": False, "message": "Invalid PIN."}
    except Exception as e:
        print(f"Error during login: {e}")
        return {"success": False, "message": "Login failed due to a server error."}

# Example: Simulating a user signup with reCAPTCHA validation
def signup_user(token, user_data):
    if verify_recaptcha(token):
        # Save user information to Turso after successful reCAPTCHA
        return save_user_to_turso(user_data)
    else:
        return {"success": False, "message": "Invalid reCAPTCHA, signup failed."}


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