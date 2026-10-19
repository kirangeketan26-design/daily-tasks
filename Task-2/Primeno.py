# Program to check whether a number is prime

# Take a number from the user
num = int(input("Enter a number: "))

# Assume the number is prime initially
is_prime = True

# Numbers less than 2 are not prime
if num < 2:
    is_prime = False

else:
    # Check whether any number divides num exactly
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")