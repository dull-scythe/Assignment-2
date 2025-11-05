from student_service import StudentRecords
from student_repo import StudentRepository
import random

def main():
    db = StudentRepository()
    records = StudentRecords(db)
    try: 
        records.create_table()

    except Exception as error:
        print({error})

    while True:
        print("\n------ Student Management System ------")
        print("1. Add a student")
        print("2. View Student Records")
        print("3. Delete Student")
        print("4. Exit System...")

        choice = input("Select a number to begin: ")

        if choice == "1":
            try:
                name = input("Enter student name: ").strip()
                age = int(input("Enter student age: ").strip())
                grade = int(input("Enter student grade: ").strip())
                #student_id = random.randint(1000, 9999)
                records.add_student(name, age, grade, student_id = random.randint(1000, 9999))
            except Exception as error:
                print(f"Please enter valid values for age and grade: {error}.\n")

        elif choice == "2":
            try:
                 records.get_students()
            except Exception as error:
                print(f"Unable to retrieve student data: {error}")

        elif choice == "3":
            try: 
                student_id = int(input("Enter Student ID to terminate: "))
                records.delete_student(student_id)
            except Exception as error:
                print(f"Student ID is invalid: {error}\n")

        elif choice == "4":
            print("Exiting student Management System...")
            break
        else:
            print("Invalid entry. Please try again...")


if __name__ == "__main__":
    main()
    