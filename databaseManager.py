import sqlite3
from cryptoUtilities import encrypt_password, decrypt_password

class DatabaseManager:
    def __init__(self, db_path="accounts.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()
        self.create_master_table()

    
    def create_table(self):
        query="""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR NOT NULL,
            webUrl VARCHAR NOT NULL,
            password VARCHAR NOT NULL 
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def create_master_table(self):
        query="""
        CREATE TABLE IF NOT EXISTS masterLogin (
        MasterID INTEGER PRIMARY KEY AUTOINCREMENT,
        MasterUsername VARCHAR NOT NULL,
        MasterPassword VARCHAR NOT NULL,
        ContactEmail VARCHAR NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def create_vault_table(self):
        query="""
        CREATE TABLE IF NOT EXISTS vault (
        id 
        VaultId INTEGER PRIMARY KEY AUTOINCREMENT,
        MasterID INTEGER FOREIGN KEY REFERENCES masterLogin(MasterID),
        id INTEGER FOREIGN KEY REFERENCES accounts(id)
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_account(self, username, webUrl, password, MasterPassword):
        query="INSERT INTO accounts (username, webUrl, password) VALUES (?, ?, ?)"
        encryptedPassword = encrypt_password(password, MasterPassword)
        self.conn.execute(query, (username, webUrl, encryptedPassword))
        self.conn.commit()

    def insert_master(self, MasterUsername, MasterPassword, ContactEmail):
        query="INSERT INTO masterLogin (MasterUsername, MasterPassword, ContactEmail) VALUES (?, ?, ?)"
        self.conn.execute(query, (MasterUsername, MasterPassword, ContactEmail))
        self.conn.commit()

    def delete_account_by_id(self, account_id):
        query="DELETE FROM accounts WHERE id = ?"
        self.conn.execute(query, (account_id,))
        self.conn.commit()

    
    def get_account_by_id(self, account_id):
        query = "SELECT id, username, webUrl, password FROM accounts WHERE id = ?"
        cursor = self.conn.execute(query, (account_id,))
        row = cursor.fetchone()

        from account import Account 
        if row:
            id, username, webUrl, password = row
            password = float(password)
            return Account(id, username, webUrl, password)
        
        return None

    def get_master_account(self, username, password):
        query = "SELECT MasterID, Masterusername, MasterPassword FROM masterLogin WHERE MasterUsername = ? AND MasterPassword = ?"
        cursor = self.conn.execute(query, (username, password,))
        row = cursor.fetchone()
        
        if row:
            return row
        
        return None