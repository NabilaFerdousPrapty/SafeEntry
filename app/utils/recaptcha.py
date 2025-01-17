import requests
from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel

app = FastAPI()

RECAPTCHA_SECRET_KEY = "6LdN17gqAAAAAI5DQ28TKl9IXLKAb2lwrWnlojJw"

def verify_recaptcha(recaptcha_response: str):
    payload = {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", data=payload)
    result = response.json()
    return result.get("success", False)

@app.post("/submit")
async def submit_form(recaptcha_response: str = Form(...)):
    # Verify reCAPTCHA
    if not verify_recaptcha(recaptcha_response):
        raise HTTPException(status_code=400, detail="reCAPTCHA verification failed.")
    return {"message": "Form submitted successfully!"}
