#这个文件里专门写函数
import sqlite3

def save_expense(amount, category, description, created_at):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expense(amount, category, description, created_at)
    VALUES (?, ?, ?, ?)
    """, (amount, category, description, created_at))

    conn.commit()
    conn.close()

def get_all_expenses():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, amount, category, description, created_at
        FROM expense
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    expenses = []

    for row in rows:
        expenses.append({
            # "amount": row[0],
            # "category": row[1],
            # "description": row[2],
            # "created_at": row[3]
            "id": row[0],
            "amount": row[1],
            "category": row[2],
            "description": row[3],
            "created_at": row[4]
        })

    conn.close()

    return expenses


def stats_expenses():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expense
        GROUP BY category
        ORDER BY category
    """)

    rows = cursor.fetchall()

    category_stats = []
    for row in rows:
        category_stats.append({
            "category": row[0],
            "total": row[1]
        })

    conn.close()

    return category_stats

def delete_expense(expense_id):
    conn = sqlite3.connect("expense.db")
    #游标（中文翻译）
    cursor =conn.cursor()

    cursor.execute(
        """
        SELECT FROM expense
        WHERE id = ?
        """,
        (expense_id,)
    )

    conn.commit()
    conn.close()
    print("deleted successfully")

def edite_expense(expense_id,amount,category,description):
    conn = sqlite3.connect("expense.db")
    #游标（中文翻译）
    cursor =conn.cursor()

    cursor.execute(
        """
        UPDATE expense
        SET amount = ?,
            category =?,
            description =?,
        WHERE id =?    
        """,
        (
            amount,
            category,
            description,
            expense_id
        )
    )

    conn.commit()
    conn.close()
    print("expense edited successfully")

