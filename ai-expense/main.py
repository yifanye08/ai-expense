# file for practice cursor commit
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from ai import analyze
from database import save_expense

app = FastAPI()

class ExpenseRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Expense API is running"}

@app.post("/expense")
def create_expense(req: ExpenseRequest):
    data = analyze(req.text)

    save_expense(
        amount=data["amount"],
        category=data["category"],
        description=data["description"],
        created_at=str(datetime.now().date())
    )

    return {
        "status": "success",
        "data": data
    }