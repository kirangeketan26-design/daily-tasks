# Ask the user to enter a whole number
number = int(input("Enter a number: "))

# Use the remainder operator to check if the number divides by 2
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")