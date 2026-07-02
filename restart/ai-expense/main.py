#file for practice cursor commit
from openai import OpenAI

client = OpenAI(
    api_key="sk-3efc8d3cbd954982a874e0fc433c0e96",
    base_url="https://api.deepseek.com"
)

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

输出格式：
分类：xxx
总结：xxx
"""
            }
        ]
    )
    return res.choices[0].message.content


while True:
    text = input("输入消费（q退出）：")

    if text == "q":
        break

    print("\nAI分析：")
    print(analyze(text))
    print("-" * 30)