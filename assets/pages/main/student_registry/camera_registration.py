from assets.backend.process.camera import Camera
import customtkinter as ctk

class Camera_Frame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
       
        # Right Frame 
        right_frame = ctk.CTkFrame(self, width=400, height=600, fg_color='#252525')
        
        # Top Frame Widgets
        right_top_frame = ctk.CTkFrame(right_frame, width=400, height=300, fg_color='#252525')
        self.camera = Camera(right_top_frame, 400,300) # Camera Object
        self.camera.stop_camera()
        
        # Bottom Frame Instance
        right_bottom_frame = ctk.CTkFrame(right_frame, width=400, height=300, fg_color='#252525')
        
        # Grid Declaration for Bottom Frame
        for column in range(4):
            right_bottom_frame.grid_columnconfigure(column, weight=1)
        for row in range(5):
            right_bottom_frame.grid_rowconfigure(row, weight=1)
        
        # Bottom Frame Widgets
        capture_btn = ctk.CTkButton(right_bottom_frame, text="Capture", command=lambda :self.camera.capture_photo('student_number'), width=100, height=40, fg_color="#3a3a3a", hover_color="#0096C9")
        open_camera_btn = ctk.CTkButton(right_bottom_frame, text="Open Cam", command=lambda :self.camera.start_camera(), width=100, height=40, fg_color="#3a3a3a", hover_color="#36BB01") 
        reset_btn = ctk.CTkButton(right_bottom_frame, text="Reset", command=lambda: self.camera.remove_photo('student_number'), width=100, height=40, fg_color="#3a3a3a", hover_color="#C90102")
        capture_btn.grid(row=0, column=1, padx=3, pady=3)
        open_camera_btn.grid(row=0, column=2, padx=3, pady=3)
        reset_btn.grid(row=0, column=3, padx=3, pady=3)
        
        # Left Frame
        left_frame = ctk.CTkFrame(self, width=500, height=600, fg_color='transparent')
        
        left_top_frame = ctk.CTkFrame(left_frame, width=400, height=300, fg_color='transparent')
        left_bottom_frame = ctk.CTkFrame(left_frame, width=400, height=300, fg_color='transparent')
        
        # Grid Declaration for Left Frame
        for column in range(4):
            left_top_frame.grid_columnconfigure(column, weight=1)
            left_bottom_frame.grid_columnconfigure(column, weight=1)
        for row in range(13):
            left_top_frame.grid_rowconfigure(row, weight=1)
            left_bottom_frame.grid_rowconfigure(row, weight=1)
        
        # Left Frame Widgets
        
        section_label = ctk.CTkLabel(left_top_frame, text="Student Details Confirmation ", text_color='white', font=('anonymous pro', 15, 'bold'))
        # Label dictionary for confirmation display (used for layout/reference)
        confirm_label_dict = {
            'full_name_label': 'Full Name : ',
            'birthday_label': 'Birthday : ',
            'age_label': 'Age : ',
            'phone_number_label': 'Phone Number : ',
            'address_label': 'Address : ',
            'guardian_name_label': 'Guardian Name : ',
            'guardian_no_label': 'Guardian No. : ',
            'student_number_label': 'Student Number : '
        }
        
        self.confirm_label = {}

        for key, text in confirm_label_dict.items():
            label = ctk.CTkLabel(left_top_frame, text=text, text_color='white', font=('anonymous pro', 14, 'bold'))
            if key == 'student_number_label':
                label.configure(text_color='yellow')
            self.confirm_label[key] = label

        # Add the Widgets to the left top frame 

        section_label.grid(row=1, column=1, columnspan=2, pady=(30,0), sticky='nsew')

        # Grid Labels for the Student Demographics
        row_value = 3
        for key, value in self.confirm_label.items():
            value.grid(row=row_value, column=1, padx=2, sticky='w')
            row_value += 1
            
        
        # Left bottom Frame
        # Back button 
        back_btn = ctk.CTkButton(left_bottom_frame, text='Back', width=100, height=40, fg_color="#3a3a3a", hover_color="#C90102", command=lambda: self.controller.switch_frame('Student_Registration'))
        back_btn.grid(row=12, column=0)
        
        # Pack Right Frames
        right_frame.pack(side="right", fill='y') # Pack the frame for the right side
        right_top_frame.pack(side="top", fill="both") # Top Frame
        right_bottom_frame.pack(side="bottom", fill="both") # Bottom Frame
        
        # Propagate Frames for the right frame
        right_top_frame.pack_propagate(False)  # Prevent frame from resizing to fit its contents
        right_bottom_frame.grid_propagate(False)
        
        # Pack Left frames
        left_top_frame.pack(side="top", fill="both")
        left_bottom_frame.pack(side="bottom", fill="both") # Bottom Frame
        
        # Propagate Frames for the left frame
        left_frame.pack(side="left", fill="y")
        left_top_frame.grid_propagate(False)
        left_bottom_frame.grid_propagate(False)
       
        # Pack the Camera
        self.camera.pack(expand=True, fill="both")
        
        
        