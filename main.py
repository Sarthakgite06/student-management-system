from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Routes.StudentRoutes import router as student_router

app = FastAPI()

# CORS Configuration
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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