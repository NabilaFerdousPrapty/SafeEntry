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
        return True
    else:
        print("Error: Invalid reCAPTCHA")
        return False
