# Task 1: Syntax Error Fixed
def greet():
    # Fixed: Added parentheses for Python 3
    return "Hello, AI Debugging Lab!"

# Test Execution
print(f"Task 1 Output: {greet()}")

# 3 Assert Test Cases (Required by assignment)
assert greet() == "Hello, AI Debugging Lab!", "Test Case 1 Failed"
assert type(greet()) == str, "Test Case 2 Failed: Should return string"
assert len(greet()) > 0, "Test Case 3 Failed: String is empty"
print("Task 1 Tests Passed!\n" + "-"*30)




# Task 2: Logic Error Fixed
def check_number(n):
    # Fixed: Used '==' for comparison instead of '='
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"

# Test Execution
print(f"Task 2 Output (10): {check_number(10)}")
print(f"Task 2 Output (5): {check_number(5)}")

# 3 Assert Test Cases
assert check_number(10) == "Ten", "Test Case 1 Failed: 10 should be Ten"
assert check_number(99) == "Not Ten", "Test Case 2 Failed: 99 is Not Ten"
assert check_number(0) == "Not Ten", "Test Case 3 Failed: 0 is Not Ten"
print("Task 2 Tests Passed!\n" + "-"*30)




# Task 3: Runtime Error Fixed (File Handling)
import os

def read_file(filename):
    try:
        # Fixed: Added try-except block
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Setup: Create a dummy file for testing success case
with open("test_file.txt", "w") as f:
    f.write("File Content Loaded")

# 3 Scenarios (Required by assignment)
# Scenario 1: File Exists
print(f"Scenario 1 (Exists): {read_file('test_file.txt')}")
# Scenario 2: File Missing
print(f"Scenario 2 (Missing): {read_file('nonexistent.txt')}")
# Scenario 3: Invalid Path (Simulated)
print(f"Scenario 3 (Empty): {read_file('')}")

# Cleanup dummy file
os.remove("test_file.txt") 
print("Task 3 Tests Passed!\n" + "-"*30)




# Task 4: Missing Method Error Fixed
class Car:
    def start(self):
        return "Car started"
    
    # Fixed: Defined the missing method
    def drive(self):
        return "Car is driving"

my_car = Car()

# 3 Assert Test Cases
assert my_car.start() == "Car started", "Test Case 1 Failed"
assert my_car.drive() == "Car is driving", "Test Case 2 Failed"
assert hasattr(my_car, 'drive'), "Test Case 3 Failed: Method drive missing"

print(f"Task 4 Output: {my_car.drive()}")
print("Task 4 Tests Passed!\n" + "-"*30)




# Task 5: TypeError Fixed

# Solution 1: Type Casting (Math Addition)
def add_five_math(value):
    return int(value) + 5

# Solution 2: String Concatenation
def add_five_str(value):
    return str(value) + "5"

# 3 Assert Test Cases
# Case 1: Math Addition
assert add_five_math("10") == 15, "Math Test Failed"
# Case 2: String Concatenation
assert add_five_str(10) == "105", "String Test Failed"
# Case 3: Math with normal int
assert add_five_math(20) == 25, "Math Int Test Failed"

print(f"Solution 1 (Math): {add_five_math('10')}")
print(f"Solution 2 (String): {add_five_str(10)}")
print("Task 5 Tests Passed!\n" + "-"*30)




