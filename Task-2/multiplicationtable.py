# Program to print the multiplication table of a number

# Take a number from the user
num = int(input("Enter a number: "))

# Repeat the loop 10 times
for i in range(1, 11):

    # Calculate and display the multiplication
    print(num, "x", i, "=", num * i)