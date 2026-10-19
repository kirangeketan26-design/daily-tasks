# Task 6: Read and Write Data Using Files

# Function to write student details to a file
def write_data():

    print("\nEnter Student Details")

    # Take student information
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")

    try:
        # Open the file in write mode
        with open("students.txt", "w") as file:

            # Write student details into the file
            file.write("Student Name: " + name + "\n")
            file.write("Student Marks: " + marks + "\n")

        print("\nData written successfully!")

    except OSError:
        print("Error while writing data to the file.")


# Function to read student details from a file
def read_data():

    try:
        # Open the file in read mode
        with open("students.txt", "r") as file:

            # Read the contents of the file
            data = file.read()

        print("\n----- Student Details -----")
        print(data)

    except FileNotFoundError:
        print("File not found! Please save student data first.")

    except OSError:
        print("Error while reading the file.")


# Main program
while True:

    print("\n===== STUDENT FILE MANAGEMENT =====")
    print("1. Write Student Data")
    print("2. Read Student Data")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_data()

    elif choice == "2":
        read_data()

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")