from student_repo import StudentRepository
import random

class StudentRecords:
    def __init__(self, db):
        self.student_info = StudentRepository()

    def add_student(self, name, age, grade, student_id):
        if age > 15 and grade > 70:
                try: 
                    self.student_info.add_student(name, age, grade, student_id)
                    #print(f"Student {name} added successfully with ID: {student_id}\n")
                except Exception as error:
                    print(f"Unable to add student due to {error}.")
        else:
            print(f"Student needs to be atleast 16 years old and have a grade higher than")
    
    def get_students(self):
            try:
                students = self.student_info.get_students()
                if not students:
                    print(f"No students found.\n")
                else:
                    print("\n ----- Student List -----")
                    for student in students:
                        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade {student[3]}")
                    print()
                    
            except Exception as error:
                print(f"Unable to retrieve {error} at this time.\n")

    def delete_student(self, student_id):
        try:
            if student_id < 1000: 
                 raise ValueError
            elif student_id > 1000: 
                self.student_info.delete_student(student_id)
                print(f"Student {student_id} has been deleted.\n")
        except ValueError:
              print(f"Invalid Student ID. Please try again.")

    
