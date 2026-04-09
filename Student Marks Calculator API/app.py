from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model
class Student(BaseModel):
    name: str
    marks: List[int]

# Route
@app.post("/result")
def calculate_result(student: Student):
    total = sum(student.marks)
    avg = total / len(student.marks)

    result = "Pass" if avg >= 40 else "Fail"

    return {
        "name": student.name,
        "total": total,
        "average": avg,
        "result": result
    }
