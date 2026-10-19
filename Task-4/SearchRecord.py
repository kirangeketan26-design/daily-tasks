# Task 2: Search for a Student Record by ID or Name

# Store some student records in a list
students = [
    {"id": "101", "name": "Rahul", "marks": 85},
    {"id": "102", "name": "Amit", "marks": 92},
    {"id": "103", "name": "Priya", "marks": 78},
    {"id": "104", "name": "Sneha", "marks": 88}
]

# Ask the user what they want to search for
search_value = input("Enter student ID or name to search: ")

# Assume the record has not been found
found = False

# Check each student record
for student in students:

    # Compare the entered value with the ID or name
    if (student["id"] == search_value
            or student["name"].lower() == search_value.lower()):

        print("\nStudent Record Found!")
        print("Student ID:", student["id"])
        print("Student Name:", student["name"])
        print("Student Marks:", student["marks"])

        found = True

# Display a message if no record matches
if found == False:
    print("Student record not found.")