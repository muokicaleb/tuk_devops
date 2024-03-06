from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/divide")
def divide_numbers(numbers: Numbers):
    if numbers.b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": numbers.a / numbers.b}
