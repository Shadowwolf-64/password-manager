import sqlite3

class DatabaseManager:
    def __init__(self, db_path="accounts.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    
    def create_table(self):
        query="""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            balance REAL NOT NULL 
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    
    def insert_account(self, username, email, balance):
        query="INSERT INTO accounts (username, email, balance) VALUES (?, ?, ?)"
        self.conn.execute(query, (username, email, balance))
        self.conn.commit()

    
    def get_account_by_id(self, account_id):
        query = "SELECT id, username, email, balance FROM accounts WHERE id = ?"
        cursor = self.conn.execute(query, (account_id,))
        row = cursor.fetchone()
        from account import Account

        if row:
            id, username, email, balance = row
            balance = float(balance)
            return Account(id, username, email, balance)
        
        return None