import cv2
import os
import customtkinter as ctk
from PIL import Image, ImageTk

class Camera(ctk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master)
        
        self.width = width
        self.height = height
        
        self.video_label = ctk.CTkLabel(self, text="")
        self.video_label.pack()
        
        self.cam = None
        self.running = False
        self.current_frame = None

    def start_camera(self):
        if not self.running:
            self.cam = cv2.VideoCapture(0)
            self.running = True
            self.update_frame()


    def stop_camera(self):
        if self.cam:
            self.running = False
            self.cam.release()
            cv2.destroyAllWindows()
            self.cam = None
            self.video_label.configure(image=None)
            print("Camera stopped.")

    def update_frame(self):
        if self.running and self.cam:
            ret, frame = self.cam.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ctk.CTkImage(light_image=img, dark_image=img, size=(self.width, self.height))
                self.video_label.configure(image=imgtk)
                self.video_label.imgtk = imgtk
                self.current_frame = frame

                # Force GUI to update
                self.video_label.update_idletasks()
                self.update_idletasks()
                self.update()
        self.after(10, self.update_frame)

    def capture_photo(self, student_number):
        if self.current_frame is not None:
            img_name = f"assets/img/student_img/{student_number}.png"
            cv2.imwrite(img_name, cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2BGR))
            print(f"Photo saved as {student_number}")
            self.stop_camera()

    def remove_photo(self, student_number):
        img_name = f"assets/img/student_img/{student_number}.png"
        if os.path.exists(img_name):
            os.remove(img_name)
            print(f"Photo {student_number} removed")
        else:
            print(f"Photo {student_number} does not exist")
            self.stop_camera()       
    
            
