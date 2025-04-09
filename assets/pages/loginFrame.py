from PIL import Image
from assets.backend.auth.login_authentication import Authentication
from assets.backend.env.encryption import Encryption
import customtkinter as ctk
import rsa
    
class Login(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.encryption = Encryption()
            
        # Main frame Configuration
        self.configure(width=350, 
                       height=350,
                       corner_radius=30)
        self.pack_propagate(False)
        
        # Main sub Frame components
        self.image_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.login_frame = ctk.CTkFrame(self, fg_color='transparent')
        
        # Image Frame Components
        try: 
            icon = Image.open(r'./assets/img/login_page/white_admin_icon.png')
            self.ctk_icon = ctk.CTkImage(light_image=icon, size=(60,60))
            self.admin_icon = ctk.CTkLabel(self.image_frame, image=self.ctk_icon, text='')
            self.admin_icon.grid(row=1, column=0, pady=(25,10), padx=(10,0))
        except FileNotFoundError:
            print(f"A problem occur upon opening administrator icon")  
             
        # Login Frame Componenents
        self.account_heading = ctk.CTkLabel(self.login_frame, text='Account', font=('Arial', 14, 'bold'))
        self.account_entry = ctk.CTkEntry(self.login_frame, placeholder_text='Account Number') # Set 1
        self.account_password_heading = ctk.CTkLabel(self.login_frame, text='Password', font=('Arial', 14, 'bold'))
        self.account_password_entry = ctk.CTkEntry(self.login_frame, placeholder_text='Password') # Set 2

        self.submit_button = ctk.CTkButton(self.login_frame, height=40, width=250, text= 'Login') # Button
        # Configuration for the login components
        self.account_entry.configure(height=40, width=250)
        self.account_password_entry.configure(height=40, width=250, show='•')
        self.submit_button.configure(font=('Arial', 14, 'bold'), command=self.fetch_data)
    
        # Define a Grid for the login frame
        self.login_frame.grid_columnconfigure(0, weight=1) # Number of Columns
        for i in range (6): # Number of Rows 
            self.login_frame.grid_rowconfigure(i, weight=1) 

        components_dictionary = {
            1 : ['account_heading', 'account_entry'], # Account Number Pair
            2 : ['account_password_heading', 'account_password_entry'], # Account Password Pair
        }
        
        for key in components_dictionary.keys():
            for value in components_dictionary[key]:
                if value == 'account_heading' or value == 'account_password_heading':
                    getattr(self, value).grid(row=key*2-1, column=0, padx=10, pady=(10,0), sticky='ew')
                else :
                    getattr(self, value).grid(row=key*2, column=0, padx=10, pady=5, sticky='ew')
        self.submit_button.grid(row = 6, column=0, padx=10, pady=15, sticky='ew')
    
        # Add the sub frames in main frame
        self.image_frame.pack()
        self.login_frame.pack()
            
    def fetch_data(self):
        if self.account_entry.get() == '' or self.account_password_entry.get() == '':
            print("Please fill in all fields")
            return
        
        self.admin_account = self.account_entry.get()
        self.admin_password = self.account_password_entry.get()
        
        # Encrypt the data
        self.admin_encrypted_acc, self.admin_encrypted_password, = self.encryption.encrypt_data(self.admin_account, self.admin_password)
        
        # Create an instance of the Authentication class
        self.auth = Authentication(self.admin_encrypted_acc, self.admin_encrypted_password)
        
        # Clear tghe entry fields after fetching the data
        self.account_entry.delete(0, ctk.END)
        self.account_password_entry.delete(0, ctk.END)
        
        