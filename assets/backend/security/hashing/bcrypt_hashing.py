from assets.backend.config.connection import Connection
from assets.backend.security.encryption.rsa_decryption import Decryption
import bcrypt

class Hash:
    @staticmethod
    def hash_password(password: str) -> bytes:
        """Hash a password using bcrypt."""
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password  # Return as bytes (no need for decoding)

    def check_password(self, rsa_password: str, hashed_password: bytes) -> bool:
        """Check if the provided password matches the hashed password."""
        # Load the private key
        decrypted_password = Decryption.single_decryption(rsa_password)
        
        print(f"Password: {rsa_password}")
        print(f"Hashed Password: {hashed_password}")
        # Check password by comparing the plain password with the hashed password
        return bcrypt.checkpw(decrypted_password.encode('utf-8'), hashed_password.encode('utf-8'))
