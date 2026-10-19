# Student Record Management System
# Day 4 Python Internship Project

import json
import os

# File used to store student records
FILE_NAME = "students.json"


# --------------------------------
# Function to load student records
# --------------------------------

def load_records():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                records = json.load(file)

            if not isinstance(records, list):
                print("Invalid file format. Starting with empty records.")
                return []

            # Validate the basic structure of every record
            for record in records:
                if not isinstance(record, dict):
                    print("Invalid record format. Starting with empty records.")
                    return []

                if not all(
                    key in record
                    for key in ["id", "name", "marks"]
                ):
                    print("Invalid record format. Starting with empty records.")
                    return []

            print("Records loaded successfully!")
            return records

        except (json.JSONDecodeError, OSError):
            print("Unable to read the file. Starting with empty records.")

    return []


# --------------------------------
# Function to save student records
# --------------------------------

def save_records(records):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(records, file, indent=4)

        print("Records saved successfully!")

    except OSError:
        print("Error: Unable to save records.")


# --------------------------------
# Function to add a student
# --------------------------------

def add_student(records):
    print("\n--- Add Student Record ---")

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    # Check for duplicate IDs
    for student in records:
        if student["id"].lower() == student_id.lower():
            print("Student ID already exists!")
            return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        marks = float(input("Enter student marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid input! Please enter numerical marks.")
        return

    # Create a dictionary for the student
    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    # Add the dictionary to the list
    records.append(student)

    print("Student added successfully!")


# --------------------------------
# Function to display all students
# --------------------------------

def display_students(records):
    print("\n--- All Student Records ---")

    if not records:
        print("No student records available.")
        return

    for student in records:
        print("--------------------------------")
        print("Student ID:", student["id"])
        print("Student Name:", student["name"])
        print("Student Marks:", student["marks"])


# --------------------------------
# Function to search for a student
# --------------------------------

def search_student(records):
    print("\n--- Search Student ---")

    search_value = input(
        "Enter student ID or name: "
    ).strip().lower()

    if not search_value:
        print("Please enter an ID or name.")
        return

    found = False

    for student in records:
        if (
            student["id"].lower() == search_value
            or search_value in student["name"].lower()
        ):
            print("\nStudent Found!")
            print("Student ID:", student["id"])
            print("Student Name:", student["name"])
            print("Student Marks:", student["marks"])

            found = True

    if not found:
        print("Student record not found.")


# --------------------------------
# Function to sort by name
# --------------------------------

def sort_by_name(records):
    sorted_records = sorted(
        records,
        key=lambda student: student["name"].lower()
    )

    print("\n--- Students Sorted by Name ---")
    display_students(sorted_records)


# --------------------------------
# Function to sort by marks
# --------------------------------

def sort_by_marks(records):
    sorted_records = sorted(
        records,
        key=lambda student: student["marks"],
        reverse=True
    )

    print("\n--- Students Sorted by Marks ---")
    display_students(sorted_records)


# --------------------------------
# Function to update student details
# --------------------------------

def update_student(records):
    print("\n--- Update Student Record ---")

    student_id = input("Enter student ID to update: ").strip()

    for student in records:
        if student["id"].lower() == student_id.lower():

            print("Student found:", student["name"])

            new_name = input(
                "Enter new name (press Enter to keep current name): "
            ).strip()

            if new_name:
                student["name"] = new_name

            new_marks = input(
                "Enter new marks (press Enter to keep current marks): "
            ).strip()

            if new_marks:
                try:
                    marks = float(new_marks)

                    if marks < 0 or marks > 100:
                        print("Marks must be between 0 and 100.")
                        return

                    student["marks"] = marks

                except ValueError:
                    print("Invalid marks! Update cancelled.")
                    return

            print("Student record updated successfully!")
            return

    print("Student ID not found.")


# --------------------------------
# Function to delete a student
# --------------------------------

def delete_student(records):
    print("\n--- Delete Student Record ---")

    student_id = input("Enter student ID to delete: ").strip()

    for student in records:
        if student["id"].lower() == student_id.lower():

            confirmation = input(
                "Are you sure you want to delete this record? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                records.remove(student)
                print("Student record deleted successfully!")

            else:
                print("Deletion cancelled.")

            return

    print("Student ID not found.")


# --------------------------------
# Function to demonstrate lists
# and dictionaries
# --------------------------------

def demonstrate_collections():
    print("\n--- List and Dictionary Demonstration ---")

    # Example of a list
    student_names = ["Rahul", "Amit", "Priya"]

    print("Original list:", student_names)

    student_names.append("Sneha")
    print("After adding a name:", student_names)

    student_names.sort()
    print("Sorted list:", student_names)

    # Example of a tuple
    student_info = ("S101", "Rahul", 85)

    print("\nExample tuple:", student_info)
    print("Name from tuple:", student_info[1])

    # Example of a set
    marks = {85, 90, 85, 75, 90}

    print("\nSet containing unique marks:", marks)

    # Example of a dictionary
    student = {
        "id": "S101",
        "name": "Rahul",
        "marks": 85
    }

    print("\nOriginal dictionary:", student)

    student["marks"] = 95
    print("Updated dictionary:", student)

    # Dictionary comprehension
    names = ["Rahul", "Amit", "Priya"]
    marks_list = [85, 92, 78]

    student_marks = {
        names[i]: marks_list[i]
        for i in range(len(names))
    }

    print("\nDictionary comprehension:", student_marks)


# --------------------------------
# Main application
# --------------------------------

def main():

    # Load existing records when the program starts
    records = load_records()

    while True:

        print("\n========================================")
        print("   STUDENT RECORD MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student Record")
        print("2. Display All Students")
        print("3. Search Student by ID or Name")
        print("4. Sort Students by Name")
        print("5. Sort Students by Marks")
        print("6. Update Student Record")
        print("7. Delete Student Record")
        print("8. Save Records to File")
        print("9. Load Records from File")
        print("10. List and Dictionary Demonstration")
        print("11. Exit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(records)

        elif choice == "2":
            display_students(records)

        elif choice == "3":
            search_student(records)

        elif choice == "4":
            sort_by_name(records)

        elif choice == "5":
            sort_by_marks(records)

        elif choice == "6":
            update_student(records)

        elif choice == "7":
            delete_student(records)

        elif choice == "8":
            save_records(records)

        elif choice == "9":
            records = load_records()

        elif choice == "10":
            demonstrate_collections()

        elif choice == "11":
            save_records(records)
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 11.")


# Start the program
if __name__ == "__main__":
    main()