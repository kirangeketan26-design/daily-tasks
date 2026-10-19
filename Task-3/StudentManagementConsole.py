# Student Management System using OOP in Python

# Parent class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Student class inherits from Person
class Student(Person):

    def __init__(self, name, age, roll_no, course, marks):
        super().__init__(name, age)

        self.roll_no = roll_no
        self.course = course
        self.__marks = marks

    # Display student details
    def display_details(self):
        print("\nStudent Details")
        print("--------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Marks:", self.__marks)

    # Update student marks
    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully!")
        else:
            print("Marks must be between 0 and 100.")


# Employee class inherits from Person
class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    # Display employee details
    def display_details(self):
        print("\nEmployee Details")
        print("--------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Student Management class
class StudentManagement:

    def __init__(self):
        # Store student objects in a list
        self.students = []

    # Add a new student
    def add_student(self):
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        roll_no = input("Enter roll number: ")
        course = input("Enter course: ")
        marks = float(input("Enter marks (0-100): "))

        # Validate age and marks
        if age < 0 or not 0 <= marks <= 100:
            print("Invalid age or marks.")
            return

        # Check for duplicate roll number
        for student in self.students:
            if student.roll_no == roll_no:
                print("Roll number already exists.")
                return

        # Create student object
        student = Student(name, age, roll_no, course, marks)

        # Add student to the list
        self.students.append(student)

        print("Student added successfully!")

    # Display all students
    def display_students(self):
        if len(self.students) == 0:
            print("No students found.")
            return

        for student in self.students:
            student.display_details()

    # Search for a student
    def search_student(self):
        roll_no = input("Enter roll number to search: ")

        for student in self.students:
            if student.roll_no == roll_no:
                student.display_details()
                return

        print("Student not found.")

    # Update student marks
    def update_student(self):
        roll_no = input("Enter roll number: ")

        for student in self.students:
            if student.roll_no == roll_no:
                marks = float(input("Enter new marks: "))
                student.update_marks(marks)
                return

        print("Student not found.")

    # Delete a student
    def delete_student(self):
        roll_no = input("Enter roll number to delete: ")

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found.")


# Main program
app = StudentManagement()

# Display menu repeatedly
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        app.add_student()

    elif choice == "2":
        app.display_students()

    elif choice == "3":
        app.search_student()

    elif choice == "4":
        app.update_student()

    elif choice == "5":
        app.delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")