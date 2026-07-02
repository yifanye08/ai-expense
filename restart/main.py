#day 1
#im trying to learn python
# print("I'm back.")
#day 2
#im trying to get the echo from the computer wordle
#name = input("请输入你的名字:")
#print("Hello,"+name+"!")

# expense = []
# while True:
#     item = input("请输入一笔支出（输入q退出）:")
#     if item == "q":
#         break
#     expense.append(item)
# print("what is your expense?")
# print(expense)

# expense = []
# while True:
#     item = input("请输入一笔支出（输入q退出）:")
#     if item == "q":
#         break
#     expense.append(int(item))
# print("all your expense:")
# for e in expense:
#     print(e)
#     total = sum(expense)
#     avg = total/len(expense)
# print("total expense:",total)
# print("average expense:",avg)


#关于写接口
# from fastapi import FastAPI

# app = FastAPI()

# expenses = []

# @app.get("/")
# def home():
#     return {"message": "Expense API is running"}

# @app.post("/add")
# def add_expense(amount: int):
#     expenses.append(amount)
#     return {"status": "ok", "all_expenses": expenses}

# @app.get("/total")
# def get_total():
#     return {"total": sum(expenses)}


#你现在学到的核心能力（很重要）

# 你已经在用真实后端结构：

# ✔ API
# @app.get / @app.post
# ✔ 数据持久化
# json 文件
# ✔ 读写文件
# open / json.load / json.dump
# 💡 这一步的意义

# 你现在已经不是在写：

# ❌ Python 小练习

# 而是在做：

# ✅ 一个“最小后端系统（MVP）”
# from fastapi import FastAPI
# import json
# import os

# app = FastAPI()

# FILE = "expenses.json"


# # ---------- 工具函数 ----------
# def load_data():
#     if not os.path.exists(FILE):
#         return []
#     with open(FILE, "r") as f:
#         return json.load(f)


# def save_data(data):
#     with open(FILE, "w") as f:
#         json.dump(data, f)


# # ---------- API ----------
# @app.get("/")
# def home():
#     return {"message": "v6 Expense API running"}


# @app.post("/add")
# def add_expense(amount: int):
#     data = load_data()
#     data.append(amount)
#     save_data(data)
#     return {"status": "ok", "data": data}


# @app.get("/list")
# def list_expenses():
#     return {"data": load_data()}


# @app.get("/total")
# def total():
#     data = load_data()
#     return {"total": sum(data)}


from openai import OpenAI

client = OpenAI(api_key="你的API_KEY")

def analyze(text):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"帮我分类并总结这笔消费：{text}"}
        ]
    )
    return res.choices[0].message.content


while True:
    text = input("输入消费（q退出）：")

    if text == "q":
        break

    print(analyze(text))