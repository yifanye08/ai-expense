# file for practice cursor commit
from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from datetime import datetime

from app.services.ai_service import analyze
from app.database.db import save_expense,get_all_expenses,stats_expenses,delete_expense,edite_expense


app = FastAPI()

templates = Jinja2Templates(directory="templates")
#这是路由
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )
#这是路由
@app.get("/expenses", response_class=HTMLResponse)
def expense_list(request: Request):
    #用database.py里的函数get_all_expense 把从数据库sqlite3里的数据赋到expenses里
    expenses = get_all_expenses()
    #expenses里的数据送到到expenses.html页面里
    return templates.TemplateResponse(
        "expenses.html",
        {
            "request": request,
            #左边 "expenses" 是模板里使用的变量名，右边 expenses 是 Python 里的变量
            "expenses": expenses
            
        }
    )   

@app.get("/stats", response_class=HTMLResponse)
def stats_sum(request: Request):
    #用database.py里的函数get_all_expense 把从数据库sqlite3里的数据赋到expenses里
    category_stats = stats_expenses()
    return templates.TemplateResponse(
        "stats.html",
        {
            "request": request,
            "category_stats": category_stats
        }
    )   
# class ExpenseRequest(BaseModel):
#     text: str

@app.post("/expense")
def create_expense(text: str = Form(...)):
    
    data = analyze(text)

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

@app.get("/delete/{expense_id}")
def delete(expense_id: int):

    delete_expense(expense_id)

    return RedirectResponse(
        "/expenses",
        status_code=303
    )

@app.get("/edite/{expense_id},{amount},{category},{description}")
def edite(expense_id: int,amount:dou,category:chr,description:chr):

    edite_expense(expense_id,amount,category,description)
    return RedirectResponse(
        "/expenses",
        status_code=303
    )