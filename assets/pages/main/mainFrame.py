import customtkinter as ctk
from PIL import Image
class Main_Frame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        '''Sub Frame Initization''' 
        # Self Configure
        
        self.controller = controller
        
        self.configure(
                    width=900,
                    height=600
        )
        
        # Sub Frames Declaration
        self.left_frame = ctk.CTkFrame(self, fg_color='#262626', 
                                       height=600, 
                                       width=270
                                       )
        self.right_frame = ctk.CTkFrame(self, fg_color='#393839', 
                                        height=600, 
                                        width=630
                                        )
        
        # Content for the left frame
        self.top_frame = ctk.CTkFrame(self.left_frame, 
                                      fg_color='transparent', 
                                      height=250, 
                                      width=250,
                                      corner_radius=20
                                      ) 
        self.bottom_frame = ctk.CTkFrame(self.left_frame, 
                                        fg_color='transparent',
                                        height=350,
                                        width=270,
                                        corner_radius=20
                                        )
        
        # Define Grid for the Left Top Frame
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        
        # Widgets for the top frame in the left frame
        raw_image = Image.open(r'assets/img/main_page/black_school_logo.png')
        school_img = ctk.CTkImage(light_image=raw_image, size=(180, 220))
        school_logo = ctk.CTkLabel(self.top_frame, image=school_img, text='')
        school_logo.grid(row=0, column=0, padx =10, pady=(10, 10))
        
        # Widgets for the bottom frame in the left frame 

        # Define Grid for the bottom frame
        self.bottom_frame.grid_columnconfigure(0, weight=1)
            
        for rows in range(7):
            self.bottom_frame.grid_rowconfigure(rows, weight=2)
        
        # Bottom button initialization
        self.student_records_btn = ctk.CTkButton(self.bottom_frame, text='Student Records',command=lambda: self.controller.switch_frame('Student_Registration'))
        self.search_btn = ctk.CTkButton(self.bottom_frame, text='Search')
        self.statistics_btn = ctk.CTkButton(self.bottom_frame, text='Statistic')
        self.settings_btn = ctk.CTkButton(self.bottom_frame, text='Settings')
        self.help_btn = ctk.CTkButton(self.bottom_frame, text='Help')
        self.exit_btn = ctk.CTkButton(self.bottom_frame, text='Exit', command=lambda: self.controller.switch_frame('Login'))
    
        # Inserted the buttons to list for initialization
        buttons_list = [
            self.student_records_btn,
            self.search_btn,
            self.statistics_btn,
            self.settings_btn,
            self.help_btn,
            self.exit_btn
        ]

        # 3. Grid them (DO NOT create new buttons inside the loop)
        for i, button in enumerate(buttons_list):
            button.grid(row=i+1, column=0, padx=5, pady=5, sticky='nsew')
        
        '''Frame Packing on this Section'''
        # Insert the Frame to the Master Frame 
        self.left_frame.pack(side='left', fill='both', expand=True)
        self.right_frame.pack(side='right', fill='both', expand=True)
        # Insert the sub frame for the left_frame
        self.top_frame.pack(side='top', fill='both', expand=True)
        self.bottom_frame.pack(side='bottom', fill='both', expand=True)
        