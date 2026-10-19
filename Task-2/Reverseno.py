# Program to reverse a number

# Take a number from the user
num = int(input("Enter a number: "))

# Initialize reversed number with 0
reverse = 0

# Repeat until the number becomes 0
while num > 0:

    # Get the last digit
    digit = num % 10

    # Add the digit to the reversed number
    reverse = reverse * 10 + digit

    # Remove the last digit from the original number
    num = num // 10

# Display the reversed number
print("Reversed number is:", reverse)