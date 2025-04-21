from assets.backend.process.id_gen_backend.camera import Camera
from assets.backend.process.id_gen_backend.generate_qr import QRCodeGenerator
from assets.backend.process.id_gen_backend.generate_id import GenerateID
from assets.backend.process.id_gen_backend.signature import SignaturePopup
from assets.backend.process.data_insertion.student_db import Student_Database

import customtkinter as ctk

class Camera_Frame(ctk.CTkFrame):
    def __init__(self, master, controller, student_data = None):
        super().__init__(master)
        self.student_db = Student_Database()
        self.controller = controller
        self.student_data = student_data
        self.qr_gen = QRCodeGenerator()    
        self.id_gen = GenerateID()    
       
        # Right Frame 
        self.right_frame = ctk.CTkFrame(self, width=450, height=600, fg_color='#252525')
        
        self.camera = Camera(self.right_frame, 400,300) # Camera Object
        self.camera.stop_camera()

        # Grid Declaration for Right Frame
        for column in range(4):
            self.right_frame.grid_columnconfigure(column, weight=1)
        for row in range(10):
            self.right_frame.grid_rowconfigure(row, weight=1)
            
        # Button Declaration
        capture_btn = ctk.CTkButton(self.right_frame, text="Capture", command=lambda :self.camera.capture_photo(self.student_number), width=100, height=40, fg_color="#3a3a3a", hover_color="#0096C9")
        open_camera_btn = ctk.CTkButton(self.right_frame, text="Open Cam", command=lambda :self.camera.start_camera(), width=100, height=40, fg_color="#3a3a3a", hover_color="#36BB01") 
        reset_btn = ctk.CTkButton(self.right_frame, text="Reset", command=lambda: self.camera.remove_photo('student_number'), width=100, height=40, fg_color="#3a3a3a", hover_color="#C90102")
        finish_btn = ctk.CTkButton(self.right_frame, text="Finish", command=self.finish_btn, width=100, height=40, fg_color="#3a3a3a", hover_color="#0096C9")
        
        # Button Grid
        capture_btn.grid(row=6, column=1, padx=3, pady=3, sticky='w')
        open_camera_btn.grid(row=6, column=2, padx=3, pady=3, sticky='w')
        reset_btn.grid(row=6, column=3, padx=3, pady=3, sticky='w')
        finish_btn.grid(row=9, column=3, padx=3, pady=3, sticky='w')
        
        # Left Frame
        self.left_frame = ctk.CTkFrame(self, width=450, height=600, fg_color='transparent')
        
        # Grid Declaration for Left Frame
        for column in range(4):
            self.left_frame.grid_columnconfigure(column, weight=1)
        for row in range(13):
            self.left_frame.grid_rowconfigure(row, weight=1)
    
        # Left Frame Widgets
        section_label = ctk.CTkLabel(self.left_frame, text="Student Details Confirmation ", text_color='white', font=('anonymous pro', 15, 'bold'))
        # Label dictionary for confirmation display (used for layout/reference)
        confirm_label_dict = {
            'full_name_label': 'Full Name : ',
            'birthday_label': 'Birthday : ',
            'course_label': 'Course : ',
            'phone_number_label': 'Phone Number : ',
            'guardian_name_label': 'Guardian Name : ',
            'guardian_no_label': 'Guardian No. : ',
            'address_label': 'Address : ',
            'student_number_label': 'Student Number : '
        }
        
        # Grid Labels for the Student Demographics (LABELS)
        self.confirm_label = {}

        for key, text in confirm_label_dict.items():
            label = ctk.CTkLabel(self.left_frame, text=text, text_color='white', font=('anonymous pro', 14, 'bold'))
            if key == 'student_number_label':
                label.configure(text_color='yellow')
            self.confirm_label[key] = label

        # Add the Widgets to the left top frame 
        section_label.grid(row=1, column=0, columnspan=4, pady=(30,0), sticky='nsew')

        row_value = 3
        for key, value in self.confirm_label.items():
            value.grid(row=row_value, column=1, padx=20, sticky='w')
            row_value += 1
            
        # Back button 
        back_btn = ctk.CTkButton(self.left_frame, text='Back', width=100, height=40, fg_color="#3a3a3a", hover_color="#C90102", command=lambda: self.controller.switch_frame('Student_Registration'))
        back_btn.grid(row=12, column=0)
        
        # Pack Right Frames
        self.right_frame.pack(side="right", fill='y') # Pack the frame for the right side
        
        # Propagate Frames for the right frame
        self.right_frame.pack_propagate(False)  # Prevent frame from resizing to fit its contents
        self.right_frame.grid_propagate(False)
        
        # Propagate Frames for the left frame
        self.left_frame.pack(side="left", fill="y")
        self.left_frame.grid_propagate(False)
       
        # Pack the Camera
        self.camera.pack(expand=True, fill="both")
        
    # Data Receiver
    def receive_data(self, student_data) :
        self.student_data = student_data
        row_value = 3
        for key, text in self.student_data.items():
            if key == 'first_name_entry' or key == 'last_name_entry' or key == 'middle_name_entry':
                continue
            else :
                label = ctk.CTkLabel(self.left_frame, text=text, text_color='white', font=('anonymous pro', 14, 'bold'))

                if key == 'student_number':
                    self.student_number = text
                    label.configure(text_color='yellow')

                label.grid(row=row_value, column=2, padx=20, sticky='w')
                row_value += 1
    
    def finish_btn(self):
        self.student_db.insert_data(self.student_data)
        self.qr_gen.generete_qr(self.student_number, self.student_data['fullname'])
        signature_window = SignaturePopup(self, self.student_number)
        self.wait_window(signature_window)
        self.id_gen.generate_id(self.student_data)
        self.controller.switch_frame('Main_Menu')
    