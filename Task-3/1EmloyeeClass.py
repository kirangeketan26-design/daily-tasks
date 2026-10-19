# Program to create an Employee class

class Employee:

    # Constructor to initialize employee details
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    # Method to display employee details
    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Monthly Salary:", self.salary)

    # Method to calculate annual salary
    def annual_salary(self):
        return self.salary * 12


# Create an employee object
employee1 = Employee("Rahul", 1001, 25000)

# Display employee details
employee1.display_details()

# Calculate and display annual salary
print("Annual Salary:", employee1.annual_salary())