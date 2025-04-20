from assets.backend.security.encryption.rsa_decryption import Decryption
from assets.backend.security.hashing.bcrypt_hashing import Hash
from assets.backend.config.connection import Connection
import time

class Authentication:
    def __init__(self, account_Number, password):
        self.account_Number = account_Number
        self.password = password
        self.decryption = Decryption()
        self.connection = Connection()   
        self.hash = Hash()
        
        self.time_taken = 0.0  
            
        self.login_status = self.authenticate()
        
        
    def authenticate(self):
        valid = False
        db = self.connection.connect()
        cursor = db.cursor()
        
        try:
            query = "SELECT admin_account, password_hash FROM administrator"
            cursor.execute(query)
            results = cursor.fetchall()

            for result in results :
                start_time = time.perf_counter()
                self.decrypted_account_no = self.decryption.decrypt_data(result[0], self.account_Number)
                self.decrypted_account_password = self.hash.check_password(self.password, result[1])
                
                end_time = time.perf_counter()
                self.time_taken += end_time - start_time
                
                print(f"Decrypted Account Number: {self.decrypted_account_no}")
                print(f"Decrypted Account Password: {self.decrypted_account_password}")
                 
                if self.decrypted_account_no and self.decrypted_account_password:
                    valid = True
                    break    
            
            if valid:
                print ("✅ Login Successful")
                print(f"⏳ Checking Time : {self.time_taken}")
                return True
            else :
                print(f"⏳ Checking Time : {self.time_taken}")
                print ("❌ Login Failed - Invalid Credentials")
                return False
        finally:
            cursor.close()
            db.close()
            