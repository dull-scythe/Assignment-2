import random

class Student:
    def __init__(self, name=None, age=None, grade=None, student_id = None):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id


    def add_student(self, name, age, grade, student_id):
        return print(f"Name: {name}, Age: {age}, Grade: {grade}, ID: {student_id}")
    





