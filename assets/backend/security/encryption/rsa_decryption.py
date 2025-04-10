from assets.backend.config.connection import Connection
import rsa
import base64

class Decryption:
    def decrypt_data(self, db_accounts_stored_base64, encrypted_account_no_base64):
        # Load the private key
        with open('assets/backend/security/encryption/keys/private_key.pem', 'rb') as private_key_file:
            private_key = rsa.PrivateKey.load_pkcs1(private_key_file.read())
        
        # Decrypt the data from the database
        # First, decode the Base64 encoded data from the database (which is stored as Base64)
        db_decrypted_account_no_bytes = base64.b64decode(db_accounts_stored_base64)  # Decode from Base64
        db_decrypted_account_no = rsa.decrypt(db_decrypted_account_no_bytes, private_key).decode('utf-8')  # Then, decrypt with RSA

        # Decrypt the provided account number
        # Decode the provided Base64 string (not encode again, just decode)
        decrypted_account_no_bytes = base64.b64decode(encrypted_account_no_base64)
        decrypted_account_no = rsa.decrypt(decrypted_account_no_bytes, private_key).decode('utf-8')

        # Compare the decrypted account numbers
        if db_decrypted_account_no == decrypted_account_no:
            return True
        else:
            return False
    
    @staticmethod
    def single_decryption(decrypted_admin_password_bytes):
        # Load the private key
        with open('assets/backend/security/encryption/keys/private_key.pem', 'rb') as private_key_file:
            private_key = rsa.PrivateKey.load_pkcs1(private_key_file.read())
            
        # Decode the Base64 encoded password (which is stored as Base64)
        decrypted_account_no_bytes = base64.b64decode(decrypted_admin_password_bytes)
        decrypted_password = rsa.decrypt(decrypted_account_no_bytes, private_key).decode('utf-8')
        
        return decrypted_password

        