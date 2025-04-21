from assets.backend.config.connection import Connection
from assets.backend.process.id_gen_backend.genereate_student_num import StudentNumberGenerator
from assets.pages.main.student_registry.camera_registration import Camera_Frame
import customtkinter as ctk

class Register_Student(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller   
        
        self.student_information = []

        # Self Configuration
        self.configure(width=700, height=500, corner_radius=15, fg_color='#252525')
        
        # Initialize a Main Frame
        self.main_frame = ctk.CTkFrame(self, fg_color='#252525',height=480,width=680,corner_radius=15) 
                    
        # Create Grid for the main frame`           
        for column in range(6):
            if column == 4 :
                 self.main_frame.grid_columnconfigure(column, weight=2)
                 continue
            self.main_frame.grid_columnconfigure(column, weight=1)
        for row in range(13):
            self.main_frame.grid_rowconfigure(row, weight=1)
        
        # Store label variables to initialize labels faster
        label_dict = {
            'first_name_label': 'First Name : ',
            'last_name_label': 'Last Name : ',
            'middle_name_label': 'Middle Name : ',
            'birthday_label': 'Birthday : ',
            'course_label': 'Course : ',
            'contact_no_label': 'Contact No. : ',
            'guardian_name_label': 'Guardinan Name : ', 
            'guardian_no_label': 'Guardian No. : ',
            'address_label': 'Address : '
        }
        
        # Store entry variables to initialize labels faster
        entry_dict = {
            'first_name_entry': 'First Name',
            'last_name_entry': 'Last Name',
            'middle_name_entry': 'Middle Name',
            'birthday_entry': 'Birthday (YYYY-MM-DD)',
            'course_entry': 'Course',
            'contact_no_entry': 'Contact No.',
            'guardian_name_entry': 'Guardian Name', 
            'guardian_no_entry': 'Guardian No.',
            'address_entry': 'Address'
        }
        
        # Store buttons in a dictionary for faster initialization
        btn_dict = {
            'back_btn':'Back', 
            'next_btn':'Next'
        }
        
        # Control for grid layout
        row = 2
        column = 0

        # Store labels and entry in empty dictionary to access for later
        self.label = {}
        self.entry = {}
        self.btn = {}
        
        # Main label for the whole Registration 
        main_label = ctk.CTkLabel(self.main_frame, text='Student Demographics Registration', text_color='white', font=('anonymous pro', 18, 'bold'))
        main_label.grid(row=1, column=0, columnspan=6)
        
        for key, value in label_dict.items() :
            label = ctk.CTkLabel(self.main_frame, text=value, text_color='white', font=('anonymous pro', 14, 'bold'))
            self.label[key] = label
            if key == 'address_entry':
                label.grid(row=row, column=3, pady=1, sticky='ne', columnspan=2, rowspan=2)
                continue
            label.grid(row=row, column=2, pady=1, sticky='e')
            row += 1      
            
        row = 2
        for key, value in entry_dict.items() :
            entry = ctk.CTkEntry(self.main_frame, placeholder_text=value)
            self.entry[key] = entry
            if key == 'address_entry':
                entry.grid(row=row, column=3, pady=1, sticky='nsew', columnspan=2, rowspan=2)
                continue
            entry.grid(row=row, column=3, pady=1, sticky='ew', columnspan=2)
            row += 1
        
        for key, value in btn_dict.items()  :
            btn = ctk.CTkButton(self.main_frame, text=value, width=100, height=40, fg_color="#3a3a3a", hover_color="#0096C9")
            self.btn[key] = btn
            btn.grid(row=13, column=column, pady=1, sticky='nsew', columnspan=1)
            column += 5
            
        self.btn['next_btn'].configure(command=self.next_btn)
        self.btn['back_btn'].configure(command=self.back_btn, hover_color="#C90102",)
            
        
        # Propagate the main frame and the self frame to false                              
        self.pack_propagate(False)
        self.main_frame.pack()      
        self.main_frame.grid_propagate(False)
        
    def back_btn(self):
        self.controller.switch_frame('Main_Menu')

    def next_btn(self):
        fetch_student_data = {}
        for key, value in self.entry.items():
            if value.get() == '':
                print(f"Please fill the Information {key}")
                return
            
            if key == 'first_name_entry':
                first_name = value.get()
            elif key == 'last_name_entry':
                last_name = value.get()
            elif key == 'middle_name_entry':
                middle_name = value.get()
                fetch_student_data['fullname'] = first_name + ' ' + last_name + ', ' + ' ' +  middle_name 
            fetch_student_data[key] = value.get()

        student_no = StudentNumberGenerator.student_number_generator()
        fetch_student_data['student_number'] = student_no        
            
        self.controller.switch_frame_data_transfer('Camera_Frame', fetch_student_data)