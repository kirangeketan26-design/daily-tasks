# Program to create a Student class

# Create a class
class Student:

    # Create a method to initialize student details
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    # Create a method to display student details
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)


# Create an object of the Student class
student1 = Student("Ketan", 101, "Computer Engineering")

# Call the method
student1.display_details()