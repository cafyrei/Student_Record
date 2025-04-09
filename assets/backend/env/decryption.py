import rsa

class Decryption:
    def decrypt_data(self, encrypted_account_no, encrypted_account_password):
        # Load the private key
        with open('assets/backend/env/keys/private_key.pem', 'rb') as private_key_file:
            private_key = rsa.PrivateKey.load_pkcs1(private_key_file.read())
        
        # Decrypt the data
        decrypted_account_no = rsa.decrypt(encrypted_account_no, private_key).decode()
        decrypted_account_password = rsa.decrypt(encrypted_account_password, private_key).decode()
        
        return decrypted_account_no, decrypted_account_password