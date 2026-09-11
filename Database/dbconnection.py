import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
mongodb_url = os.getenv("MongoDB_URL")

connectionstring = MongoClient(mongodb_url)

database = connectionstring["student_management"]

collection = database["studentsdb"]
# mongodb+srv://sarthakgite006_db_user:<db_password>@cluster0.rdpej7d.mongodb.net/?appName=Cluster0