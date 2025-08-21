class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"
    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Marks    : {self.marks}")
        print(f"Grade    : {self.calculate_grade()}")
# Taking input from user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))
# Creating Student object and displaying details
student = Student(name, roll_no, marks)
student.display_details()





