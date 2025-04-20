from assets.backend.config.connection import Connection
from PIL import Image
import customtkinter as ctk

class Search(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        
        # Tools needed for searching
        self.controller = controller   # Page Controller
        self.connection = Connection() # MySQL connection
        
        # Main Frame Configuration
        self.configure(width=900, height=600, fg_color='transparent')
        self.pack_propagate()
        
        # Main sub frame declaration
        self.search_frame= ctk.CTkFrame(self, height=100, width=900, fg_color='transparent')
        self.search_frame.grid_propagate()
        
        self.header_frame= ctk.CTkFrame(self, height=40, width=900)
        
        self.display_frame= ctk.CTkScrollableFrame(self, height=460, width=900, fg_color='transparent')
        
        # Load Resources for Search Frame
        # For Button Image
        try :
            raw_icon = Image.open(r'assets/img/search/search.png')
            search_icon = ctk.CTkImage(light_image=raw_icon, size=(25,25))
        except FileNotFoundError:
            print(f'Error Loading Search Image {FileNotFoundError}')
        
        # For Option Menu
        filter_options = ('Sort by A-Z', 'Sort by Z-A')
        selected_option = ctk.StringVar(value='Sort by A-Z')
        
        # Search Frame 
        label = ctk.CTkLabel(self.search_frame, text='Search Student', fg_color='red')
        
        self.back_btn = ctk.CTkButton(self.search_frame, height=40, width=30, text='Back', command=lambda: self.controller.switch_frame('Main_Menu'))
        self.search_label = ctk.CTkLabel(self.search_frame, text='Search Student', font=('Cascadia code', 16, 'bold'))
        self.search_bar = ctk.CTkEntry(self.search_frame, placeholder_text='Search Student',height=40, width=400)
        self.search_btn = ctk.CTkButton(self.search_frame, height=40, width=30, text='Search',image= search_icon, command=self.search_process)
        self.search_filter = ctk.CTkOptionMenu(self.search_frame, variable=selected_option, height=40, width=30,values=filter_options)
        
        # Load Database and Enter
        headers = ["Student No.", "First Name", "Middle Name", "Last Name", "Phone Number", "Birthday", "Nationality"]
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(self.header_frame, text=header, fg_color="gray20", width=120)
            label.grid(row=0, column=col, padx=4, pady=5)
        
        # Call Function to Display Data
        self.fetch_data_db()
        
        
        # Add Griding Lines to the search frame
        for column in range(5):
            if column == 2:
                self.search_frame.columnconfigure(column, weight=2)
                continue
            self.search_frame.columnconfigure(column, weight=1)  
            
        for row in range(2):
            self.search_frame.rowconfigure(row, weight=1)
        
        # Add the widgets to the Search frame by Grid Layout
        self.back_btn.grid(column=1, row=1, sticky='w')
        self.search_label.grid(column=2, row=0, sticky='w')
        self.search_bar.grid(column=2, row=1, sticky='we')
        self.search_btn.grid(column=3, row=1, sticky='e')
        self.search_filter.grid(column=4, row=1, sticky='w')
        
        # Sub Frame Pack
        self.search_frame.pack(fill='both', expand=True, pady=20)
        self.header_frame.pack(fill='both', expand=True)
        self.display_frame.pack(fill='both', expand=True, pady=10)
        
    def fetch_data_db(self):
        db = self.connection.connect()
        cursor = db.cursor()
        
        try: 
            query = 'SELECT student_number, first_name, middle_name, last_name, phone_no, date_of_birth, nationality FROM student_records'
            cursor.execute(query)
            results = cursor.fetchall()
            
            # Display all the values in the database
            for row_index, row_data in enumerate(results, start=1):
                for col_index, cell_data in enumerate(row_data):
                    cell = ctk.CTkLabel(self.display_frame, text=str(cell_data), width=120)
                    cell.grid(row=row_index, column=col_index, padx=3, pady=1) 
        # Close Connection avoiding Leakages
        finally:
            cursor.close()
            db.close()
        
    def search_process(self):
        
        # Define Database Tools
        db = self.connection.connect()
        cursor = db.cursor()
        
        if self.search_bar.get() =='':
            print("Please fill the search bar")
            return

        # Clear the latest prompt
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        if self.search_bar.get() == 'all':
            self.fetch_data_db()


        search = self.search_bar.get()
        self.search_bar.delete(0, ctk.END)
        
        try:
            query = 'SELECT student_number, first_name, middle_name, last_name, phone_no, date_of_birth, nationality FROM student_records WHERE last_name = %s'
            cursor.execute(query, (search,))
            results = cursor.fetchall()
            
            if results:
                for row_index, row_data in enumerate(results, start=1):
                    for col_index, cell_data in enumerate(row_data):
                        cell = ctk.CTkLabel(self.display_frame, text=str(cell_data), width=120)
                        cell.grid(row=row_index, column=col_index, padx=3, pady=1)
            else :
                print(f"Student with {search} is not found!")
                self.fetch_data_db()
            
        finally:
            # Close Connection avoiding Leakages
            cursor.close()
            db.close()

        