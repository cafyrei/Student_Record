import json
import mysql.connector
from datetime import datetime

class Connection:
    def connect(self):
        try:
            with open('.vscode/settings.json', 'r') as f:
                data = json.load(f)

            detail = data['sqltools.connections'][0]
            self.port = detail.get('port', '')
            self.name = detail.get('name', '')
            self.host = detail.get('server', '')
            self.database = detail.get('database', '')
            self.user = detail.get('username', '')
            self.password = detail.get('password', '')
            self.auth_plugin = detail.get('auth_plugin', '')

            self.db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                auth_plugin=self.auth_plugin
            )

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
