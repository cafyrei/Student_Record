import json
import mysql.connector

class Connection:
        
    def connect(self):
        with open('.vscode/settings.json', 'r') as f:
            data = json.load(f)
        
        details = data['sqltools.connections']
        
        
        for detail in details:
            self.name = detail.get('name', '')
            self.host = detail.get('server', '')
            self.user = detail.get('user', '')
            self.password = detail.get('password','')
            self.port = detail.get('port', '') 
        
        print(self.name)
        
        try :    
            self.db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port
            )
            return self.db
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
    