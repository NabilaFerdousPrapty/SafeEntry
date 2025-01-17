import requests

def verify_recaptcha(token):
    secret_key = '6Le2RboqAAAAAPEvG8lZgOsNstsk3TX38AIAw5SL'  
    payload = {
        'secret': secret_key,
        'response': token
    }

    # Send a POST request to Google reCAPTCHA API to verify the token
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)

    # Parse the JSON response
    result = response.json()

    # Log the response for debugging
    print("reCAPTCHA Response:", result)

    # Log any error codes if present
    if 'error-codes' in result:
        print("Error Codes:", result['error-codes'])

    # Check if the response indicates success
    if result.get('success'):
        print("reCAPTCHA verification succeeded")
        return True
    else:
        print("Error: Invalid reCAPTCHA")
        return False


# Example: Simulating a user signup with reCAPTCHA validation
def signup_user(token):
    if verify_recaptcha(token):
        # Proceed with the signup logic (e.g., storing user data in the database)
        return {"success": True, "message": "Signup successful!"}
    else:
        return {"success": False, "message": "Invalid reCAPTCHA, signup failed."}


