# Task 01: Mutable Default Argument (Function Bug)
# Prompt Given to AI: "Analyze the provided Python code where a mutable default argument causes unexpected behavior."

def add_item(item, items=None):
    # FIXED: Use None as default to avoid shared state
    if items is None:
        items = []
    items.append(item)
    return items

# Testing
print(f"Task 1 Output 1: {add_item(1)}") # Output: [1]
print(f"Task 1 Output 2: {add_item(2)}") # Output: [2] (Correctly creates a new list)
print("-" * 30)




# Task 02: Floating-Point Precision Error
# Prompt Given to AI: "Fix the floating-point comparison error in this function using a tolerance method."

import math

def check_sum():
    # FIXED: Use math.isclose for safe floating-point comparison
    # Direct comparison (0.1 + 0.2 == 0.3) fails due to precision issues
    return math.isclose(0.1 + 0.2, 0.3)

# Testing
print(f"Task 2 Output: {check_sum()}") # Output: True
print("-" * 30)




# Task 03: Recursion Error (Missing Base Case)
# Prompt Given to AI: "The provided recursion code runs infinitely. Add a base case to fix the RecursionError."

def countdown(n):
    # FIXED: Added base case to stop recursion
    if n <= 0:
        return
    print(n)
    countdown(n-1)

# Testing
print("Task 3 Output:")
countdown(5) # Output: 5 4 3 2 1
print("-" * 30)




# Task 04: Dictionary Key Error
# Prompt Given to AI: "Fix the KeyError caused by accessing a non-existent dictionary key. Use a safe retrieval method."

def get_value():
    data = {"a": 1, "b": 2}
    # FIXED: Use .get() method to handle missing keys gracefully
    return data.get("c", "Key not found")

# Testing
print(f"Task 4 Output: {get_value()}")
print("-" * 30)




# Task 05: Infinite Loop (Wrong Condition)
# Prompt Given to AI: "Identify why this loop never ends and correct the code to ensure termination."

def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1 # FIXED: Increment 'i' to update the loop condition

# Testing
print("Task 5 Output:")
loop_example() # Output: 0 1 2 3 4
print("-" * 30)



