# file for practice cursor commit
from openai import OpenAI
from database import save_expense
import os
import json

api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


def analyze(text):
    res = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": f"""
                你是一个记账助手，请完成：
                1. 分类（餐饮/交通/购物/其他）
                2. 简单总结

                消费：{text}

                请返回JSON格式：
                包含两个字段：
                - category（分类：餐饮/交通/购物/其他）
                - description（简短总结）
                """
            }
        ],
    )
    return res.choices[0].message.content


while True:
    text = input("输入消费payment（q退出）：")

    if text == "q":
        break

    print("\nAI分析：")
    result = analyze(text)
    print(result)
    data = json.loads(result)

    save_expense(
        amount=0,  # 先占位（后面我们再做金额识别）
        category=data["category"],
        description=data["description"],
        created_at="2026-07-06",
    )

    print("✔ 已保存到数据库")
    print("-" * 30)
