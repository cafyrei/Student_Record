from assets.backend.config.connection import Connection
import customtkinter as ctk

class Register_Student(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.current_frame = None
        # Self Configuration
        self.configure(width=700,
                       height=500,
                       corner_radius=15,
                       fg_color='#252525'
                       )
        self.pack_propagate(False)
        
        # Initialize a Main Frame
        self.main_frame = ctk.CTkFrame(self,
                                  fg_color='#252525',
                                  height=480,
                                  width=680,
                                  corner_radius=15,
                                  ) 
                                      
        self.main_frame.grid_propagate(False)
        
        # Define a Grid for the whole main_frame
        for column in range(7):
            self.main_frame.grid_columnconfigure(column, weight=2)
        
        for row in range(14):
            self.main_frame.grid_rowconfigure(row, weight=0)

        # Define a list of Label to quickly initialize Label       
        label_list = [
            ('registration_label', 'STUDENT REGISTRATION FORM'),
            ('age_label', 'Age')
        ]

        # Define a list of Entry to quickly initialize Entry
        entry_list = [
            ('first_name_label', 'First Name', 'first_name_entry'),
            ('last_name_label','Last Name', 'last_name_entry'),
            ('middle_name_label','Middle Name', 'middle_name_entry'),
            ('phone_number_label','Phone Number', 'contact_info_entry'),
            ('address_label','Address', 'address_entry'),
            ('nationality_label','Nationality', 'nationality_entry'),
            ('guardian_label','Guardian Name', 'guardian_entry'),
            ('guardian_no_label','Guardian No.', 'guardian_no_entry'),
            ('birthday_label','Birthday (YYYY-MM-DD)', 'birthday_entry'),
        ]
        
        # Create Label for each item in the label_list
        for i, (label_name, text) in enumerate(label_list):
            label = ctk.CTkLabel(self.main_frame, text=text)
            setattr(self.main_frame, label_name, label)
        # Genereate Drop down values for Age
        age_options = [str (i) for i in range(1,100)]
        
        self.age_dropdown = ctk.CTkComboBox(self.main_frame, values=age_options, width=55)
        self.main_frame.registration_label.configure(font=('Futura', 19, 'bold'))
        self.submit_btn = ctk.CTkButton(self.main_frame, text='Next', command=self.submit_student_registration)
        self.back_btn = ctk.CTkButton(self.main_frame, text='Back', command=lambda: self.controller.switch_frame('Main_Menu'))

        
        # Create Entry for each item in the entry_list 
        for i, (label_name, text, entry_name) in enumerate(entry_list):
            label = ctk.CTkLabel(self.main_frame, text=text) 
            entry = ctk.CTkEntry(self.main_frame, placeholder_text=text)
            setattr(self.main_frame, label_name, label)
            setattr(self.main_frame, entry_name, entry)

        # Grid layout
        self.main_frame.registration_label.grid(row=0, column=1, sticky='nsew', columnspan=5, pady=15)  
          
        self.main_frame.first_name_label.grid(row=1, column=1, sticky='w', padx=50)
        self.main_frame.first_name_entry.grid(row=2, column=1, sticky='nsew', columnspan=2, padx=50)
        
        self.main_frame.last_name_label.grid(row=1, column=3, sticky='w', padx=50)
        self.main_frame.last_name_entry.grid(row=2, column=3, sticky='nsew', columnspan=2, padx=50)
            
        self.main_frame.middle_name_label.grid(row=3, column=1, sticky='w', padx=50)
        self.main_frame.middle_name_entry.grid(row=4, column=1, sticky='nsew', columnspan=2, padx=50)
        
        self.main_frame.age_label.grid(row=3, column=3, sticky='w', padx=50)
        self.age_dropdown.grid(row=4, column=3, sticky='w', padx=50)

        self.main_frame.birthday_label.grid(row=3, column=3, sticky='e', columnspan=2, padx=50)
        self.main_frame.birthday_entry.grid(row=4, column=3, sticky='e', columnspan=2, padx=50)
        
        self.main_frame.phone_number_label.grid(row=5, column=1, sticky='w', columnspan=2, padx=50)
        self.main_frame.contact_info_entry.grid(row=6, column=1, sticky='nsew', columnspan=2, padx=50)
        
        self.main_frame.nationality_label.grid(row=5, column=3, sticky='w', columnspan=2, padx=50)
        self.main_frame.nationality_entry.grid(row=6, column=3, sticky='nsew', columnspan=2, padx=50)
        
        self.main_frame.guardian_label.grid(row=7, column=1, sticky='w', columnspan=4, padx=50)
        self.main_frame.guardian_entry.grid(row=8, column=1, sticky='we', columnspan=4, padx=50)
        
        self.main_frame.guardian_no_label.grid(row=9, column=1, sticky='w', columnspan=4, padx=50)
        self.main_frame.guardian_no_entry.grid(row=10, column=1, sticky='we', columnspan=4, padx=50)
        
        self.main_frame.address_label.grid(row=11, column=1, sticky='w', columnspan=4, padx=50)
        self.main_frame.address_entry.grid(row=12, column=1, sticky='we', columnspan=4, padx=50)
        
        self.submit_btn.grid(row=14, column=3, sticky='e', columnspan=2, pady=20, padx=50)
        self.back_btn.grid(row=14, column=1, sticky='w', columnspan=2, pady=20, padx=50)
        
        # Pack the Main Frame
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(expand=True)

            
    def submit_student_registration(self):
        print('Hellow World!')
        