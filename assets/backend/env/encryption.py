import rsa

class Encryption:
    def encrypt_data(self, account_no, account_password):
        self.account_no = account_no
        self.account_password = account_password
        
        with open('assets/backend/env/keys/public_key.pem', 'rb') as public_key_file:
            public_key = rsa.PublicKey.load_pkcs1(public_key_file.read())
        
        encrypted_account_no = rsa.encrypt(self.account_no.encode(), public_key)
        encrypted_account_password = rsa.encrypt(self.account_password.encode(), public_key)
        
        return encrypted_account_no, encrypted_account_password
        