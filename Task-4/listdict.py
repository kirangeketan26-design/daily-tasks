# Task 5: Practise Lists and Dictionaries

# Part 1: Working with Lists


print("----- Working with Lists -----")

# Create a list of student names
students = ["Rahul", "Amit", "Priya", "Sneha"]

# Display the original list
print("Original list:", students)

# Access an element from the list
print("First student:", students[0])

# Add a new student
students.append("Karan")
print("After adding a student:", students)

# Remove a student
students.remove("Amit")
print("After removing a student:", students)

# Sort the student names
students.sort()
print("Sorted student names:", students)


# -------------------------------
# Part 2: Working with Dictionaries
# -------------------------------

print("\n----- Working with Dictionaries -----")

# Create a dictionary containing student details
student = {
    "id": 101,
    "name": "Rahul",
    "marks": 85
}

# Display the dictionary
print("Student details:", student)

# Access a dictionary value
print("Student name:", student["name"])

# Update student marks
student["marks"] = 95
print("After updating marks:", student)

# Add a new key-value pair
student["city"] = "Jalgaon"
print("After adding city:", student)

# Remove a key-value pair
student.pop("city")
print("After removing city:", student)

# Display all keys and values
print("\nAll student details:")

for key, value in student.items():
    print(key, ":", value)