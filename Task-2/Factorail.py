# Program to calculate the factorial of a number

# Take a number from the user
num = int(input("Enter a number: "))

# Initialize factorial with 1
factorial = 1

# Check whether the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # Multiply numbers from 1 to num
    for i in range(1, num + 1):
        factorial = factorial * i

    # Display the result
    print("Factorial is:", factorial)