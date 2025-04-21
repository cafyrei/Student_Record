from assets.backend.config.connection import Connection

class Student_Database():
    def __init__(self):
        self.connection = Connection()
        
    def insert_data(self, data):
        db = self.connection.connect()
        cursor = db.cursor()    
        
        print(data)
        
        values = (
            data['student_number'],
            data['first_name_entry'],
            data['last_name_entry'],
            data['middle_name_entry'],
            data['contact_no_entry'],
            data['birthday_entry'],
            data['course_entry'],
            data['guardian_name_entry'],
            data['guardian_no_entry'],
            data['address_entry']
        )
            
        try : 
            query = (
                    'INSERT INTO student_records '
                    '(student_number, first_name, last_name, middle_name, phone_no, '
                    'date_of_birth, course, guardian_name, guardian_phone_no, student_address) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    )
            cursor.execute(query, values)
            db.commit()
        finally:
            cursor.close()
            db.close()

    def verify_student(self, data):
        db = None
        cursor = None
        try:
            # Ensure the database connection is established
            db = self.connection.connect()
            cursor = db.cursor() 
            
            query = 'SELECT first_name, last_name, middle_name, course FROM student_records WHERE student_number = %s'
            cursor.execute(query, (data,))  # Ensure data is passed as a tuple
            
            results = cursor.fetchall()
            
            if results:
                # If a student record is found, return the results and True
                return results, True
            else:
                # If no results are found, return None and False
                return None, False
        except Exception as e:
            print(f"Error verifying student: {e}")
            return None, False
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

            