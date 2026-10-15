
import csv


class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


class StudentManager:

    def __init__(self, filename="student.txt"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    # Add Student
    def add_student(self):

        sid = input("Enter student ID: ")

        for student in self.students:
            if student.student_id == sid:
                print("\nStudent already exists!")
                return

        name = input("Enter name: ")
        course = input("Enter course: ")

        try:
            age = int(input("Enter age: "))
            marks = float(input("Enter marks: "))

            if age <= 0:
                print("Age must be greater than zero!")
                return

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100!")
                return

        except ValueError:
            print("Invalid input! Age and marks must be numbers.")
            return

        student = Student(sid, name, age, course, marks)

        self.students.append(student)
        self.save_to_file()

        print("\nStudent added successfully!")

    # View Students
    def view_student(self):

        print("\n========= VIEW STUDENTS =========")

        if len(self.students) == 0:
            print("No students found!")
            return

        for student in self.students:
            print("\n==============================")
            print("Student ID:", student.student_id)
            print("Name:", student.name)
            print("Age:", student.age)
            print("Course:", student.course)
            print("Marks:", student.marks)
            print("==============================")

        print("\nStudents displayed successfully!")

    # Search Student
    def search_student(self):

        print("\n========= SEARCH STUDENT =========")

        sid = input("Enter student ID: ")

        for student in self.students:
            if student.student_id == sid:

                print("\nStudent found successfully!")
                print("Student ID:", student.student_id)
                print("Name:", student.name)
                print("Age:", student.age)
                print("Course:", student.course)
                print("Marks:", student.marks)

                return

        print("\nStudent not found!")

    # Update Student
    def update_student(self):

        print("\n========= UPDATE STUDENT =========")

        sid = input("Enter student ID to update: ")

        for student in self.students:
            if student.student_id == sid:

                print("\nEnter new details:")

                name = input("Enter new name: ")
                course = input("Enter new course: ")

                try:
                    age = int(input("Enter new age: "))
                    marks = float(input("Enter new marks: "))

                    if age <= 0:
                        print("Age must be greater than zero!")
                        return

                    if marks < 0 or marks > 100:
                        print("Marks must be between 0 and 100!")
                        return

                except ValueError:
                    print("Invalid input! Enter numbers for age and marks.")
                    return

                student.name = name
                student.age = age
                student.course = course
                student.marks = marks

                self.save_to_file()

                print("\nStudent updated successfully!")
                return

        print("\nStudent not found!")

    # Delete Student
    def delete_student(self):

        print("\n========= DELETE STUDENT =========")

        sid = input("Enter student ID to delete: ")

        for student in self.students:
            if student.student_id == sid:

                self.students.remove(student)
                self.save_to_file()

                print("\nStudent deleted successfully!")
                return

        print("\nStudent not found!")

    