# Task 1: Fibonacci Sequence (No Functions)
n = int(input("Enter the number of terms: "))

# Initialize first two terms
a, b = 0, 1
count = 0

print("Fibonacci Sequence:")
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print(a)
else:
    while count < n:
        print(a, end=" ")
        nth = a + b
        # Update values
        a = b
        b = nth
        count += 1
print("\n")



# Task 2: Optimized Fibonacci
n = int(input("Enter the number of terms for optimized version: "))

a, b = 0, 1
print("Fibonacci Sequence (Optimized):")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n")



# Task 3: Fibonacci with Functions
def generate_fibonacci(n):
    """
    Generates Fibonacci sequence up to n terms.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Main execution
num_terms = int(input("Enter number of terms for Function-based Fibonacci: "))
if num_terms <= 0:
    print("Please enter a positive integer")
else:
    print(f"Fibonacci Sequence: {generate_fibonacci(num_terms)}")
print("\n")



# Task 5: Iterative vs Recursive

# Iterative Approach
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Recursive Approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter number of terms for Comparison: "))

print("Iterative Output:")
fibonacci_iterative(n)

print("Recursive Output:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
print("\n")