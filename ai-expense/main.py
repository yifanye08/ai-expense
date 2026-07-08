# file for practice cursor commit
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from ai import analyze
from database import save_expense

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

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