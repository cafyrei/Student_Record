import qrcode
import customtkinter as ctk
from PIL import Image, ImageTk
from assets.backend.process.id_gen_backend.camera import Camera

class Attendance(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        
        self.controller = controller
        
        # Initialize main frames
        self.right_frame = ctk.CTkFrame(self, width=500, height=600, fg_color='#3a3a3a')
        self.left_frame = ctk.CTkFrame(self, width=500, height=600, fg_color='#3a3a3a')
        
        # Instance of the camera
        self.camera = Camera(self.left_frame, 400, 300, on_qr_data_callback=self.handle_scanned_student)
        
        # Create Grid for the frames
        for column in range(4):
            self.right_frame.grid_columnconfigure(column, weight=1)
            self.left_frame.grid_columnconfigure(column, weight=1)
        for row in range(8):
            self.right_frame.grid_rowconfigure(row, weight=1)
            self.left_frame.grid_rowconfigure(row, weight=1)
            
        # Widgets Sections
        back_btn = ctk.CTkButton(self.left_frame, text='Back', command=self.back_btn, width=100, height=40, fg_color="#3a3a3a", hover_color="#C90102")
        open_camera_btn = ctk.CTkButton(self.left_frame, text="Open Cam", command=self.open_camera, width=100, height=40, fg_color="#3a3a3a", hover_color="#36BB01") 
        
        # Grid Widgets    
        back_btn.grid(row=5, column=1, sticky='ew')
        open_camera_btn.grid(row=5, column=2, sticky='ew')
        self.camera.grid(row=1, column=0, columnspan=4, rowspan=5, padx=15, sticky='nsew')
        self.camera.configure(fg_color='#2A2B2B')
        
        # Right Frame
        self.frame = ctk.CTkFrame(self.right_frame, width=300, height=300)
        self.frame.pack(padx=20, pady=(100,30))
        
        self.name_label = ctk.CTkLabel(self.right_frame, text='', font=('Arial', 18, 'bold'))
        self.program_label = ctk.CTkLabel(self.right_frame,text='', font=('Arial', 14, 'bold'))
        self.student_no_label = ctk.CTkLabel(self.right_frame,text='', font=('Arial', 12, 'bold'))
        
        self.name_label.pack()
        self.program_label.pack()
        self.student_no_label.pack()
        # Frame pack      
        self.right_frame.pack(side='right', fill="both")
        self.left_frame.pack(side='left', fill="both")
        
        # Frame grid_propagate
        self.right_frame.grid_propagate(False)
        self.left_frame.grid_propagate(False) 
    
    def back_btn(self):
        self.camera.stop_camera()
        self.controller.switch_frame('Main_Menu')
    
    def open_camera(self):
        self.data = self.camera.start_camera_qr_mode()
        print(self.data)

    def handle_scanned_student(self, student_data, student_no):
        self.student_no = student_no
        full_name = student_data[0]+' '+ student_data[1]+' '+ student_data[2]
        program = student_data[3]
        
        print(self.student_no)
        
        self.name_label.configure(text=f"{full_name}")
        self.program_label.configure(text=f"{program}")
        self.student_no_label.configure(text=f"{self.student_no}")
            
        self.display_scanned_image()
        self.after(5000, self.clear_scanned_student)
    
    def display_scanned_image(self):
        # Clear previous image
        for widget in self.frame.winfo_children():
            widget.destroy()

        try:
            img = Image.open(f"assets/img/student_img/{self.student_no}.png")
            img = img.resize((250, 250))
            img_tk = ImageTk.PhotoImage(img)

            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(300, 300))
            label = ctk.CTkLabel(self.frame, image=ctk_img, text="")  # Use CTkImage here
            label.image = ctk_img  
            label.pack()

            label.after(5000, label.destroy)
        except FileNotFoundError:
            print("Student image not found.")

    def clear_scanned_student(self):
        self.name_label.configure(text="")
        self.program_label.configure(text="")
        self.student_no = None
