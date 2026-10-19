# Program to demonstrate inheritance

# Parent class
class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


# Child class inherits Person
class Student(Person):

    def __init__(self, name, roll_no):
        # Initialize the parent class
        super().__init__(name)

        self.roll_no = roll_no

    def display_student(self):
        self.display_name()
        print("Roll Number:", self.roll_no)


# Create a Student object
s1 = Student("Amit", 101)

# Display student details
s1.display_student()