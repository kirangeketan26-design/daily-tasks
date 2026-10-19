# Task 4: Handle Invalid Input Using Exception Handling

print("Student Marks Calculator")

try:
    # Take student details
    name = input("Enter student name: ")

    # Take marks from the user
    marks = float(input("Enter student marks (0-100): "))

    # Check whether marks are valid
    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")

    else:
        print("\nStudent Details")
        print("Name:", name)
        print("Marks:", marks)

        # Check whether the student passed or failed
        if marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

except ValueError:
    # Handle input that cannot be converted into a number
    print("Error! Please enter marks using numbers only.")

finally:
    # This block always executes
    print("Program execution completed.")