# Program to create the multiplication table (from 1 to 10) of a number

# Accept input from the user
num = int(input("Enter a number to generate its multiplication table: "))

# Loop through numbers 1 to 10
for i in range(1, 11):
    # Print the multiplication result in a formatted way
    print(f"{num} x {i} = {num * i}")
# End of the program