import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def analyze(text):
    res = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": f"""
你是记账助手，从文本中提取信息，返回JSON：

消费：{text}

只返回：
{{
  "amount": 数字,
  "category": "餐饮/交通/购物/其他",
  "description": "简短描述"
}}
"""
            }
        ]
    )

    return json.loads(res.choices[0].message.content)