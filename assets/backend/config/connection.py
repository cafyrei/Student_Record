import json
import mysql.connector
from assets.backend.env.encryption import Encryption
from datetime import datetime
import base64

class Connection:
    def connect(self):
        try:
            with open('.vscode/settings.json', 'r') as f:
                data = json.load(f)

            detail = data['sqltools.connections'][0]
            self.port = detail.get('port', '')
            self.name = detail.get('name', '')
            self.host = detail.get('server', '')
            self.user = detail.get('username', '')
            self.password = detail.get('password', '')
            self.auth_plugin = detail.get('auth_plugin', '')

            self.db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.name,
                port=self.port,
                auth_plugin=self.auth_plugin
            )
            
            
            cursor = self.db.cursor()
            
            
            cursor.execute("CREATE TABLE world (name VARCHAR(255), id INT)")
        
            username = 'super_admin'
            admin_account = "admin_master01"
            password = "admin"
            
            enc = Encryption()
            account_creation = datetime.now()
            format_time = account_creation.strftime("%Y-%m-%d %H:%M:%S")
            
            admin_encr, password_encr = enc.encrypt_data(admin_account, password)

            
            admin_encr64 = base64.b64encode(admin_encr).decode('utf-8')
            password_encr64 = base64.b64encode(password_encr).decode('utf-8')
            
            cursor.execute("INSERT INTO administrator (username, admin_account, password_hash, last_login) VALUES (%s, %s, %s, %s)", (username, admin_encr64, password_encr64, format_time))
            
            print("Data Injected")
            
            

            if self.db.is_connected():
                print("✅ Successful Connection to the database")
            else:
                print("❌ Failed Connection")

            return self.db

        except FileNotFoundError:
            print("❌ settings.json file not found.")
            return None
        except mysql.connector.Error as err:
            print(f"❌ MySQL Error: {err}")
            return None
