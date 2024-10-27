class Expense:
    def __init__(self, db):
        self.db = db

    def add_expense(self, user_id, name, amount, category):
        self.db.cur.execute("INSERT INTO expenses (user_id, name, amount, category) VALUES (?, ?, ?, ?)", (user_id, name, amount, category))
        self.db.conn.commit()

    def get_expenses(self, user_id):
        self.db.cur.execute("SELECT name, amount, category FROM expenses WHERE user_id = ?", (user_id,))
        return self.db.cur.fetchall()
