# Program to check if three numbers are in increasing order,
# decreasing order, or neither.

# Accept input from the user
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
num3 = int(input("Input third number: "))

# Check if numbers are in strictly increasing order
if num1 < num2 < num3:
    print("Increasing order")

# Check if numbers are in strictly decreasing order
elif num1 > num2 > num3:
    print("Decreasing order")

# If neither increasing nor decreasing
else:
    print("Neither increasing or decreasing order")
