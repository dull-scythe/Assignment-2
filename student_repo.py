from student import Student
import sqlite3
import random

# [Connect to Database]
conn = sqlite3.connect("Student_Repository.db")
cursor = conn.cursor()

class StudentRepository: 
    def __init__(self):
        self.student = Student()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Students(
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade INTEGER NOT NULL,
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT
                    )
                    """)
    conn.commit()


    def add_student(self, name, age, grade, student_id):
        student = Student(name, age, grade)
        try:
            self.student.add_student(name, age, grade, student_id)
            student_id = random.randint(1000, 9999)
            cursor.execute("INSERT INTO Students (name, age, grade, student_id) VALUES (?, ?, ?, ?)", 
                           (student.name, student.age, student.grade, student.student_id)
                           )
            conn.commit()
            return student.student_id
        except Exception as error:
            print(f"Error when adding student: {error}")

    def get_students(self):
        try: 
            cursor.execute("SELECT * FROM Students")
            return cursor.fetchall()
        except Exception as error:
            print(f"Unable to retrieve students: {error}")


    def delete_student(self, student_id):
        if student_id < 1000 or student_id > 9999:
            cursor.execute("SELECT * FROM Students WHERE student_id < 1000", (student_id))
        elif student_id > 1000 or student_id < 10000:
            cursor.execute("DELETE FROM Students WHERE student_id = (?)", (student_id,))
            conn.commit()
        return cursor.fetchone()



