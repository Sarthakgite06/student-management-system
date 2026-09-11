from pymongo import MongoClient

connectionstring = MongoClient("mongodb+srv://sarthakgite006_db_user:iFieWFx3CjsRE1KC@cluster0.rdpej7d.mongodb.net/?appName=Cluster0")

database = connectionstring["student_management"]

collection = database["studentsdb"]
# mongodb+srv://sarthakgite006_db_user:<db_password>@cluster0.rdpej7d.mongodb.net/?appName=Cluster0