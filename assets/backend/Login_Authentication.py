import rsa

class Authentication:
    def __init__(self, account_Number, password):
        self.account_Number = account_Number
        self.password = password
        self.login_status = False
        
        print("Before Decrypting")
        print(f"Account Number: {self.account_Number}")
        print(f"Password: {self.password}")
        
        self.decrypt_account_number, self.decrypt_account_password = self.decrypt_date(self.account_Number, self.password)
        print("After Decrypting")
        print(f"Account Number: {self.decrypt_account_number}")
        print(f"Password: {self.decrypt_account_password}")
        
    def decrypt_date(self, encrypted_account_no, encrypted_password):
        with open('./assets/backend/keys/private_key.pem', 'rb') as private_file:
            private_key = rsa.PrivateKey.load_pkcs1(private_file.read())
        # Decrypt the password using RSA private key
        decrypted_account_number = rsa.decrypt(encrypted_password, private_key)
        decrypted_account_password = rsa.decrypt(encrypted_account_no, private_key)
        # Return the decrypted values
        return decrypted_account_number.decode(), decrypted_account_password.decode()
    

