import cv2
import os
import customtkinter as ctk
from PIL import Image, ImageTk
from assets.backend.process.data_insertion.student_db import Student_Database

class Camera(ctk.CTkFrame):
    def __init__(self, master, width, height, on_qr_data_callback=None):
        super().__init__(master)
        
        self.student_db = Student_Database()
        
        self.on_qr_data_callback = on_qr_data_callback
        self.width = width
        self.height = height
        
        self.video_label = ctk.CTkLabel(self, text="")
        self.video_label.pack()
        
        self.cam = None
        self.running = False
        self.current_frame = None
        
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.configure(width=self.width, height=self.height)

    def start_camera(self):
        if not self.running:
            self.cam = cv2.VideoCapture(0)
            if not self.cam.isOpened():
                print("Error: Could not open camera.")
                return
            self.running = True
            self.update_frame()
            
    def start_camera_qr_mode(self):
        if not self.running:
            self.cam = cv2.VideoCapture(0)
            if not self.cam.isOpened():
                print("Error: Could not open camera.")
                return
            self.running = True
            self._scan_qr_loop()

    def stop_camera(self):
        if self.cam and self.running:
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
    
    def scan_qr(self):
        if not self.running:
            self.cam = cv2.VideoCapture(0)
            if not self.cam.isOpened():
                print("Error: Could not open camera.")
                return
            self.running = True
            self._scan_qr_loop()  # Start the QR scanning loop
    
    def _scan_qr_loop(self):
        validity = False
        student_data = None
        if self.running and self.cam:
            ret, frame = self.cam.read()
            if not ret:
                print("Failed to read frame!")
                return
            
            # Convert the frame to RGB format for display
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # QR code detection
            qr_detector = cv2.QRCodeDetector()
            data, bbox, _ = qr_detector.detectAndDecode(frame)
            
            if bbox is not None and len(bbox) >= 4:  # Ensure bbox has at least 4 points
                for i in range(len(bbox)):
                    cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i+1) % 4][0]), (255, 0, 0), 3)

            if data:
                # Verify student data and get results
                student_data, validity = self.student_db.verify_student(data)
            
            # Update the Tkinter label with the current frame
            img = Image.fromarray(frame_rgb)
            imgtk = ctk.CTkImage(light_image=img, dark_image=img, size=(self.width, self.height))
            self.video_label.configure(image=imgtk)
            self.video_label.imgtk = imgtk
            
            # Force GUI to update
            self.video_label.update_idletasks()
            self.update_idletasks()
            self.update()

        # If QR is valid, process it
        if validity:
            self.on_qr_scan(validity, student_data, data)
        
        # Continue scanning every 50 ms (for faster updates)
        self.after(10, self._scan_qr_loop)

    def on_qr_scan(self, validity, student_data, student_no):
        if validity: 
            data = student_data[0]
            if self.on_qr_data_callback:
                self.on_qr_data_callback(data, student_no)
        else:
            print("Invalid student")
        
        
