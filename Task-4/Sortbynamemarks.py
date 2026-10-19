# Task 3: Sort Student Records by Name or Marks

# Store student records in a list
students = [
    {"id": "101", "name": "Rahul", "marks": 85},
    {"id": "102", "name": "Amit", "marks": 92},
    {"id": "103", "name": "Priya", "marks": 78},
    {"id": "104", "name": "Sneha", "marks": 88}
]

# Display the original records
print("Original Student Records:")

for student in students:
    print(student)

# Ask the user how to sort the records
print("\nChoose a sorting option:")
print("1. Sort by Name")
print("2. Sort by Marks")

choice = input("Enter your choice: ")

# Sort records alphabetically by name
if choice == "1":

    sorted_students = sorted(
        students,
        key=lambda student: student["name"]
    )

    print("\nStudents Sorted by Name:")

    for student in sorted_students:
        print(student)

# Sort records by marks, highest to lowest
elif choice == "2":

    sorted_students = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    print("\nStudents Sorted by Marks:")

    for student in sorted_students:
        print(student)

# Handle an invalid menu choice
else:
    print("Invalid choice! Please select 1 or 2.")