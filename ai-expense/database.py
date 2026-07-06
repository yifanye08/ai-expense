import sqlite3

def save_expense(amount, category, description, created_at):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO expense
    (amount, category, description, created_at)
    VALUES (?, ?, ?, ?)
    """, (amount, category, description, created_at))
    conn.commit()
    conn.close()

    print("expense saved successfully")

