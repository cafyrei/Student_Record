import os
from PIL import Image, ImageDraw, ImageFont

class GenerateID:
    def __init__(self, student_details):
        self.student_details = student_details
        
        # Load all necessary files for ID Genereation
        try:
            student_id_layout = Image.open(r'id_layout_student.png')
        except FileNotFoundError as e:
            print(f"Error: {e}. Student Layout Not Found. Please ensure all required files are in the correct directory.")
            return
        # Load Student Photo
        try :
            student_photo = Image.open(r'student.jpg')
        except FileNotFoundError as e:
            print(f"Error: {e}. Student Image Not Found. Please ensure all required files are in the correct directory.")
            return
        
        # Load Student Signature
        try :
            student_signature = Image.open(r'logos.png')
        except FileNotFoundError as e:
            print(f"Error: {e}. Student Signature Not Found. Please ensure all required files are in the correct directory.")
            return
        
        try :
            qr_code = Image.open(r'qr.png')
        except FileNotFoundError as e:
            print(f"Error: {e}. QR Code Not Found. Please ensure all required files are in the correct directory.")
            return
        
        # Load font form student details
        try : 
            font  = ImageFont.truetype("courbd.ttf", 40)
        except OSError:
            font = ImageFont.truetype("arial.ttf", 40)
            print("Custom font not found, using default font.")
            
        # Resize the student photo to fit the ID layout
        student_photo = student_photo.resize((419,512))
        student_signature = student_signature.resize((300,100))
        qr_code = qr_code.resize((375,375))
        
        # Initialize the ImageDraw object
        draw = ImageDraw.Draw(student_id_layout)
        
        student_details = [
            "Sarthou, Rovic Christopher M.",
            "01/01/2000",
            "BSCE",
            "20210828"
        ]
        
        student_id_layout.paste(student_photo, (85, 322))
        student_id_layout.paste(student_signature, (150, 845), student_signature)   
        student_id_layout.paste(qr_code, (1010,560))   
        # Add the student details to the ID layout
        height = 437
        for student_info in student_details:
            draw.text((565, height), student_info, fill='maroon', font=font)
            height += 136
        # draw.text((570, 437), "John Doe", fill='black', font=font) 
        
        student_id_layout.save('Student_ID.png')
        student_id_layout.show()
        print("ID Generated Successfully!")