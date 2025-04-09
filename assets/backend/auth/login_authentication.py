from assets.backend.env.decryption import Decryption
from assets.backend.config.connection import Connection

class Authentication:
    def __init__(self, account_Number, password):
        self.account_Number = account_Number
        self.password = password
        self.decryption = Decryption()
        self.connection = Connection()
        
        self.db = self.connection.connect()
        if self.db is None:
            print("Failed to connect to the database.")
            return
        
        self.login_status = self.authenticate()
        
        
    def authenticate(self):
        # Decrypt the account number and password
        self.decrypted_account_no, self.decrypted_account_password = self.decryption.decrypt_data(self.account_Number, self.password)
        print(f"Decrypted Account Number: {self.decrypted_account_no}") 
        
        return True
        