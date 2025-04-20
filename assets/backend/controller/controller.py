import customtkinter
from assets.pages.loginFrame import Login
from assets.pages.main.mainFrame import Main_Frame
from assets.pages.main.search.search_frame import Search
from assets.pages.main.student_registry.student_registry import Register_Student
from assets.pages.main.student_registry.camera_registration import Camera_Frame

class Controller:
    def __init__(self, root):
        self.root = root
        self.frames = {}
        
        # Initialize Frames for Controlment 
        self.frames['Login'] = Login(root, self)
        self.frames['Main_Menu'] = Main_Frame(root, self)
        self.frames['Search'] = Search(root, self)
        self.frames['Student_Registration'] = Register_Student(root, self)
        self.frames['Camera_Frame'] = Camera_Frame(root, self)
        
        self.frames["Main_Menu"].pack(expand=True)
        
    def switch_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
            
        frame = self.frames[frame_name]
        
        print(type(frame))
        frame.pack(expand=True)
        

