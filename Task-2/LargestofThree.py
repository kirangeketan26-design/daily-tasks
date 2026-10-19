# Program to find the largest of three numbers

# Take three numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Check which number is the largest
if a >= b and a >= c:
    print("Largest number is:", a)

elif b >= a and b >= c:
    print("Largest number is:", b)

else:
    print("Largest number is:", c)