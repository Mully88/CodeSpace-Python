# Program to check whether three numbers are all equal, all different, or neither

# Accept input from the user
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
num3 = int(input("Input third number: "))

# Check if all three numbers are equal
if num1 == num2 == num3:
    print("All numbers are equal")

# Check if all three numbers are different
elif num1 != num2 and num2 != num3 and num1 != num3:
    print("All numbers are different")

# If neither all equal nor all different
else:
    print("Neither all are equal or different")
