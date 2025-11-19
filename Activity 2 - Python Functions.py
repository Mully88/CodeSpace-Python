# Python function to calculate the factorial of a number

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    The factorial of n (written as n!) is the product of all integers from 1 to n.
    Special cases:
      - Factorial of 0 is defined as 1.
      - Factorial is not defined for negative numbers.
    """
    
    # Check if the number is negative
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    # Factorial of 0 is 1
    elif n == 0:
        return 1
    
    # Calculate factorial for positive numbers
    else:
        result = 1
        # Multiply result by each number from 1 up to n
        for i in range(1, n + 1):
            result *= i
        return result

# Test the function with sample data
print("Factorial of 6 is:", factorial(6))   # Expected output: 720
print("Factorial of 0 is:", factorial(0))   # Expected output: 1
print("Factorial of -3 is:", factorial(-3)) # Expected output: Factorial is not defined for negative numbers.
