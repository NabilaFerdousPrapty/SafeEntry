import requests
from turso import Turso

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
    # Turso Database credentials (Update with your Turso credentials)
    turso_url = "YOUR_TURSO_DATABASE_URL"
    turso_token = "YOUR_TURSO_ACCESS_TOKEN"

    # Initialize Turso client
    client = Turso(turso_url, turso_token)

    # Insert user data into Turso table
    try:
        query = """
        INSERT INTO users (name, email, mobile, pin) VALUES (?, ?, ?, ?);
        """
        client.execute(query, [user_data['name'], user_data['email'], user_data['mobile'], user_data['pin']])
        print("User information saved successfully!")
        return {"success": True, "message": "User information saved successfully!"}
    except Exception as e:
        print(f"Error saving user to Turso: {e}")
        return {"success": False, "message": "Failed to save user information."}

# Example: Simulating a user signup with reCAPTCHA validation
def signup_user(token, user_data):
    if verify_recaptcha(token):
        # Save user information to Turso after successful reCAPTCHA
        return save_user_to_turso(user_data)
    else:
        return {"success": False, "message": "Invalid reCAPTCHA, signup failed."}

# Example usage
if __name__ == "__main__":
    # Simulated user signup request
    recaptcha_token = "USER_RECAPTCHA_TOKEN_FROM_FRONTEND"  # Replace with actual token
    user_info = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "mobile": "1234567890",
        "pin": "12345"  # Ensure this is hashed if storing sensitive information like PIN
    }

    result = signup_user(recaptcha_token, user_info)
    print(result)
