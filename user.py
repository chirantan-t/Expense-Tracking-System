import hashlib

class User:
    def __init__(self, db):
        self.db = db

    def register(self, name, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.db.cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_password))
            self.db.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login(self, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.db.cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, hashed_password))
        user = self.db.cur.fetchone()
        if user:
            return {"id": user[0], "name": user[1], "email": user[2]}
        return None
