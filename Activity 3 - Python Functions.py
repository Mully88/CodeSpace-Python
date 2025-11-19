# Python function to check if a number is prime

def is_prime(n):
    """
    Check if a number is prime.
    Prime numbers are greater than 1 and divisible only by 1 and themselves.
    Negative numbers, 0, and 1 are not prime.
    """

    # Prime numbers must be greater than 1
    if n <= 1:
        return False

    # Check divisibility from 2 up to the square root of n
    # If n is divisible by any of these, it's not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    # If no divisors found, the number is prime
    return True


# Test the function with sample values
print("Is 2 prime?", is_prime(2))     # Expected: True
print("Is 15 prime?", is_prime(15))   # Expected: False
print("Is 17 prime?", is_prime(17))   # Expected: True
print("Is -5 prime?", is_prime(-5))   # Expected: False
print("Is 1 prime?", is_prime(1))     # Expected: False
