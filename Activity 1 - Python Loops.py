# Program to generate Fibonacci series between 0 and 50

# Initialize the first two numbers of the Fibonacci sequence
a, b = 0, 1

# Print the first number
print(a, end=" ")

# Continue generating Fibonacci numbers until the value exceeds 50
while b <= 50:
    print(b, end=" ")   # Print the current number
    a, b = b, a + b     # Update values: next number is sum of previous two
