from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Routes.StudentRoutes import router as student_router

app = FastAPI()

# CORS Configuration - allow all origins (Netlify, localhost, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router)


@app.get("/")
def home():
    return {
        "message": "Student Management API is running successfully!"
    }