from fastapi import FastAPI
from app.routes.signup import router as signup_router
from app.routes.login import router as login_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routes
app.include_router(signup_router)
app.include_router(login_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
