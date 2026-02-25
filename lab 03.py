# Question 1: Palindrome Number (Zero-Shot)
def is_palindrome(n):
    # Convert number to string to check if it reads the same backwards
    return str(n) == str(n)[::-1]

# Test cases
num = int(input("Enter a number to check Palindrome: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is not a Palindrome")
print("-" * 20)




# Question 2: Factorial Calculation (One-Shot)
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test cases
num = int(input("Enter a number for Factorial: "))
print(f"Factorial of {num} is: {factorial(num)}")
print("-" * 20)




# Question 3: Armstrong Number (Few-Shot)
def check_armstrong(n):
    # Convert to string to find number of digits
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    
    if total == n:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"

# Test cases
num = int(input("Enter a number to check Armstrong: "))
print(f"{num}: {check_armstrong(num)}")
print("-" * 20)




# Question 4: Number Classification (Prime/Composite/Neither)
import math

def classify_number(n):
    # Input validation
    if not isinstance(n, int) or n < 0:
        return "Invalid Input: Please enter a non-negative integer."
    
    # Logic for 0 and 1 (Neither prime nor composite)
    if n == 0 or n == 1:
        return "Neither Prime nor Composite"
    
    # Check for Prime
    # Optimization: Check up to square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Composite Number"
            
    return "Prime Number"

# Test cases
try:
    num = int(input("Enter a number to classify (Prime/Composite): "))
    print(f"Result: {classify_number(num)}")
except ValueError:
    print("Please enter a valid integer.")
print("-" * 20)



# Question 5: Perfect Number Check (Zero-Shot)
def is_perfect_number(n):
    if n <= 0:
        return False
    
    # Calculate sum of proper divisors
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    
    return divisor_sum == n

# Test cases
num = int(input("Enter a number to check Perfect Number: "))
if is_perfect_number(num):
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is NOT a Perfect Number")
print("-" * 20)




# Question 6: Even/Odd Classification (Few-Shot)
def check_even_odd(n):
    try:
        # Input validation handles non-integers if passed as string
        val = int(n) 
        if val % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except ValueError:
        return "Invalid Input: Please enter an integer."

# Test cases
user_input = input("Enter a number to check Even/Odd: ")
print(f"Result: {check_even_odd(user_input)}")
print("-" * 20)