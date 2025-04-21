import random
import datetime

class StudentNumberGenerator:
    def student_number_generator():
        year = datetime.datetime.now().year
        identification = random.randint(10000, 99999)
        student_number = f"{year}{identification}"

        return student_number