# Task 1: Store and Process Student Records

# Create an empty list to store student records
students = []

# Ask how many students the user wants to enter
number = int(input("How many students do you want to add? "))

# Use a loop to enter student details
for i in range(number):

    print("\nEnter details of student", i + 1)

    # Take student details
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    # Store details in a dictionary
    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    # Add the dictionary to the list
    students.append(student)

# Display all student records
print("\n----- Student Records -----")

for student in students:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("--------------------")