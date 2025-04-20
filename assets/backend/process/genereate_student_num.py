import random
import datetime

class StudentNumberGenerator:
    def __init__(self):
        self.student_number = self.student_number_generator()
        
    def student_number_generator(self):
        year = datetime.datetime.now().year
        identification = random.randint(10000, 99999)
        student_number = f"{year}{identification}"

        return student_number