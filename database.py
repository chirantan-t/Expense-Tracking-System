import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('expenses.db', check_same_thread=False)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create user table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)

        # Create expenses table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            amount REAL,
            category TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        self.conn.commit()
