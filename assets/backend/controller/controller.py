import customtkinter
from assets.pages.loginFrame import Login
from assets.pages.main.mainFrame import Main_Frame
from assets.pages.main.search.search_frame import Search
from assets.pages.main.attendance.attendance import Attendance
from assets.pages.main.student_registry.camera_registration import Camera_Frame
from assets.pages.main.student_registry.student_registry import Register_Student

class Controller:
    def __init__(self, root ):
        self.root = root
        self.frames = {}
        
        # Initialize Frames for Controlment 
        self.frames['Login'] = Login(root, self)
        self.frames['Search'] = Search(root, self)
        self.frames['Main_Menu'] = Main_Frame(root, self)
        self.frames['Attendance'] = Attendance(root, self)
        self.frames['Camera_Frame'] = Camera_Frame(root, self)
        self.frames['Student_Registration'] = Register_Student(root, self)
        
        self.frames["Attendance"].pack(expand=True)
        
    def switch_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
            
        frame = self.frames[frame_name]
        
        frame.pack(expand=True)
    
    def switch_frame_data_transfer(self, frame_name, data):
        self.data = data
        
        for frame in self.frames.values():
            frame.pack_forget()
            
        frame = self.frames[frame_name]
        frame.receive_data(data)
        
        frame.pack(expand=True)
        
        

