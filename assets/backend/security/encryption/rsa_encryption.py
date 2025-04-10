import rsa
import base64

class Encryption:
    def encrypt_data(self, account_no) :
        self.account_no = account_no
        
        with open('assets/backend/security/encryption/keys/public_key.pem', 'rb') as public_key_file:
            public_key = rsa.PublicKey.load_pkcs1(public_key_file.read())
        
        encrypted_account_no = rsa.encrypt(self.account_no.encode(), public_key)
        encrypted_account_no_base64 = base64.b64encode(encrypted_account_no).decode('utf-8')
        
        return encrypted_account_no_base64
        
        
        