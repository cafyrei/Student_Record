import customtkinter as ctk
from assets.pages.loginFrame import Login
from assets.pages.main.mainFrame import Main_Frame
from assets.pages.main.student_registry.student_registry import Register_Student
from assets.backend.controller.controller import Controller

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Root main elements
        self.title("EduPass")
        self.geometry("900x600")
        self.resizable(True, True)
        self.iconbitmap(r'assets\img\main_page\icon.ico')
    
        # Initialize Componets
        self.start = Controller(self)
        
        
    