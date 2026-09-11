from fastapi import APIRouter, HTTPException
from controller.studentcontroller import CreateStudent
from Model.studentModel import StudentStruct
from Model.studentupdate import updateStruct
from Database.dbconnection import collection

router = APIRouter()

@router.post("/createStudent")
def create(student: StudentStruct):
    return CreateStudent(student)

@router.get("/allstudents")
def get_students():
    return list(collection.find({}, {"_id": 0}))


@router.put("/edit/{roll}")
def update_student(roll: int, student: updateStruct):
    updated_student = student.model_dump(exclude_none=True)
    if not updated_student:
        raise HTTPException(status_code=400, detail="Provide a name or age to update")

    result = collection.update_one({"roll": roll}, {"$set": updated_student})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "student updated"}



@router.delete("/delete/{roll}")
@router.delete("/delet/{roll}")
def delete_student(roll: int):
    result = collection.delete_one({"roll": roll})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "student deleted"}
    