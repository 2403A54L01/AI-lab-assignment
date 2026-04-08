"""TAsk-1
Write a Python program to manage student records (Name, Roll Number, CGPA) using a suitable data structure. 
Implement both Quick Sort and Merge Sort to sort students by CGPA in descending order. 
Generate a large dataset (1000+ records), measure execution time for both algorithms, and compare their performance. 
Also include a function to display the top 10 students based on CGPA. 
Add proper comments and print clear outputs."""
from typing import List, Dict, Union
import random
def generate_student_records(num_records: int) -> List[Dict[str, Union[str, int, float]]]:
    """Generate a list of student records with random data."""
    records = []
    for i in range(num_records):
        record = {
            "Name": f"Student_{i+1}",
            "Roll Number": i + 1,
            "CGPA": round(random.uniform(0.0, 4.0), 2)
        }
        records.append(record)
    return records
def quick_sort_students(students: List[Dict[str, Union[str, int, float]]]) -> List[Dict[str, Union[str, int, float]]]:
    """Sort students by CGPA in descending order using Quick Sort."""
    if len(students) <= 1:
        return students
    pivot = students[len(students) // 2]["CGPA"]
    left = [s for s in students if s["CGPA"] > pivot]
    middle = [s for s in students if s["CGPA"] == pivot]
    right = [s for s in students if s["CGPA"] < pivot]
    return quick_sort_students(left) + middle + quick_sort_students(right)
def merge_sort_students(students: List[Dict[str, Union[str, int, float]]]) -> List[Dict[str, Union[str, int, float]]]:
    """Sort students by CGPA in descending order using Merge Sort."""
    if len(students) <= 1:
        return students
    mid = len(students) // 2
    left = merge_sort_students(students[:mid])
    right = merge_sort_students(students[mid:])
    return merge(left, right)
def merge(left: List[Dict[str, Union[str, int, float]]], right: List[Dict[str, Union[str, int, float]]]) -> List[Dict[str, Union[str, int, float]]]:
    """Merge two lists of students sorted by CGPA in descending order."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["CGPA"] > right[j]["CGPA"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def display_top_students(students: List[Dict[str, Union[str, int, float]]], top_n: int = 10) -> None:
    """Display the top N students based on CGPA."""
    print(f"Top {top_n} Students:")
    for student in students[:top_n]:
        print(f"Name: {student['Name']}, Roll Number: {student['Roll Number']}, CGPA: {student['CGPA']}")
# Generate a large dataset of student records
student_records = generate_student_records(1000)
# Sort using Quick Sort and measure execution time
import time
start_time = time.time()
sorted_students_quick = quick_sort_students(student_records)
end_time = time.time()
print(f"Quick Sort Execution Time: {end_time - start_time:.4f} seconds")
# Sort using Merge Sort and measure execution time
start_time = time.time()
sorted_students_merge = merge_sort_students(student_records)
end_time = time.time()
print(f"Merge Sort Execution Time: {end_time - start_time:.4f} seconds")
# Display the top 10 students based on CGPA
display_top_students(sorted_students_quick)
display_top_students(sorted_students_merge)

"""Task-2
Write a Python implementation of Bubble Sort with detailed inline comments explaining each step (passes, swapping, and optimization with early stopping). 
Also include time and space complexity analysis in comments.
mplementing Bubble Sort with AI Comments
• Task: Write a Python implementation of Bubble Sort.
• Instructions:
• Students implement Bubble Sort normally.
• Ask AI to generate inline comments explaining key logic (like
swapping, passes, and termination).
• Request AI to provide time complexity analysis.
• Expected Output:
• A Bubble Sort implementation with AI-generated explanatory
comments and complexity analysis.
"""

def bubble_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Sorts a list of numbers using the Bubble Sort algorithm.

    Args:
        arr (List[Union[int, float]]): The list of numbers to be sorted.

    Returns:
        List[Union[int, float]]: The sorted list of numbers.

    Time Complexity:
        O(n^2) in the worst and average cases, where n is the number of elements in the list.
        O(n) in the best case when the list is already sorted.

    Space Complexity:
        O(1) as it is an in-place sorting algorithm.
    """
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Initialize a flag to check if any swapping occurs
        swapped = False
        # Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # If they are in the wrong order, swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set the flag to True if a swap occurred
        # If no swapping occurred, the list is already sorted
        if not swapped:
            break  # Terminate early if the list is already sorted
    return arr
# Example usage:
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Output: [11, 12, 22, 25, 34, 64, 90]


"""Task-3
Write a Python implementation of Bubble Sort with detailed inline comments explaining each step (passes, swapping, and optimization with early stopping). 
Also include time and space complexity analysis in comments.
Task 3: Quick Sort and Merge Sort Comparison
• Task: Implement Quick Sort and Merge Sort using recursion.
• Instructions:
• Provide AI with partially completed functions for recursion.
• Ask AI to complete the missing logic and add docstrings.
• Compare both algorithms on random, sorted, and reverse-sorted
lists.
• Expected Output:
• Working Quick Sort and Merge Sort implementations.
• AI-generated explanation of average, best, and worst-case
complexities
"""
def check_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to check for primality.
    Returns:        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def calculate(operation: str, num1: float, num2: float) -> float:
    """Perform basic arithmetic operations.
    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
        num1 (float): The first number.
        num2 (float): The second number.    Returns:
        float: The result of the operation.
    Raises:
        ValueError: If the operation is not supported or if division by zero is attempted.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Unsupported operation. Please use 'add', 'subtract', 'multiply', or 'divide'.")
# Example usage:
# print(calculate("add", 10, 5))  # Output: 15
# try:
#   print(calculate("divide", 10, 0))  # This will raise ValueError
#   except ValueError as e:
#   print(f"Error: {e}")
# print(check_prime(29))  # Output: True
# print(check_prime(30))  # Output: False
# print(check_prime(1))   # Output: False    

"""Task-4(Real-Time Application – Inventory Management System)
Scenario: A retail store’s inventory system contains thousands of products,
each with attributes like product ID, name, price, and stock quantity. Store staff
need to:
1. Quickly search for a product by ID or name.
2. Sort products by price or quantity for stock analysis.
Task:
• Use AI to suggest the most efficient search and sort algorithms for this
use case.
• Implement the recommended algorithms in Python.
• Justify the choice based on dataset size, update frequency, and
performance requirements.
Expected Output:
• A table mapping operation → recommended algorithm → justification.
• Working Python functions for searching and sorting the inventory"""
def search_product_by_id(inventory: List[Dict[str, Union[str, int, float]]], product_id: int) -> Dict[str, Union[str, int, float]]:
    """
    Search for a product in the inventory by its ID.

    Args:
        inventory (List[Dict[str, Union[str, int, float]]]): The list of products in the inventory.
        product_id (int): The ID of the product to search for.

    Returns:
        Dict[str, Union[str, int, float]]: The product details if found, otherwise an empty dictionary.
    """
    # Using a dictionary for O(1) average time complexity search by ID
    product_dict = {product["product_id"]: product for product in inventory}
    return product_dict.get(product_id, {})
def search_product_by_name(inventory: List[Dict[str, Union[str, int, float]]], product_name: str) -> List[Dict[str, Union[str, int, float]]]:
    """
    Search for products in the inventory by name.   
    Args:
        inventory (List[Dict[str, Union[str, int, float]]]): The list of products in the inventory.
        product_name (str): The name of the product to search for.
    Returns:
        List[Dict[str, Union[str, int, float]]]: A list of products that match the name.
    """
    # Using list comprehension for O(n) time complexity search by name
    return [product for product in inventory if product_name.lower() in product["name"].lower()]
def sort_products_by_price(inventory: List[Dict[str, Union[str, int, float]]]) -> List[Dict[str, Union[str, int, float]]]:
    """Sort products by price in ascending order.
    Args:
        inventory (List[Dict[str, Union[str, int, float]]]): The list of products in the inventory.
    Returns:
        List[Dict[str, Union[str, int, float]]]: The sorted list of products
    """    # Using Timsort (Python's built-in sort) which is efficient for real-world data
    return sorted(inventory, key=lambda x: x["price"])
def sort_products_by_quantity(inventory: List[Dict[str, Union[str, int, float]]]) -> List[Dict[str, Union[str, int, float]]]:
    """Sort products by stock quantity in ascending order.
    Args:
        inventory (List[Dict[str, Union[str, int, float]]]): The list of products in the inventory.
    Returns:
        List[Dict[str, Union[str, int, float]]]: The sorted list of products.
    """    # Using Timsort (Python's built-in sort) which is efficient for real-world data
    return sorted(inventory, key=lambda x: x["stock_quantity"])
# Example inventory data
inventory = [
    {"product_id": 1, "name": "Laptop", "price": 999.99, "stock_quantity": 10},
    {"product_id": 2, "name": "Smartphone", "price": 499.99, "stock_quantity": 50},
    {"product_id": 3, "name": "Headphones", "price": 199.99, "stock_quantity": 100},
]
# Example usage:
print(search_product_by_id(inventory, 2))  # Output: {'product_id':
# 2, 'name': 'Smartphone', 'price': 499.99, 'stock_quantity': 50}
print(search_product_by_name(inventory, "phone"))  # Output: [{'product_id':
# 2, 'name': 'Smartphone', 'price': 499.99, 'stock_quantity': 50}]
print(sort_products_by_price(inventory))  # Output: [{'product_id': 3, 'name': 'Headphones', 'price': 199.99, 'stock_quantity': 100}, {'product_id': 2, 'name': 'Smartphone', 'price': 499.99, 'stock_quantity': 50}, {'product_id': 1, 'name': 'Laptop', 'price': 999.99, 'stock_quantity': 10}]
print(sort_products_by_quantity(inventory))  # Output: [{'product_id': 1,
# 'name': 'Laptop', 'price': 999.99, 'stock_quantity': 10}, {'product_id': 2, 'name': 'Smartphone', 'price': 499.99, 'stock_quantity': 50}, {'product_id': 3, 'name': 'Headphones', 'price': 199.99, 'stock_quantity': 100}]

"""Task-5 Write a Python program to simulate stock data (Stock Symbol, Opening Price, Closing Price), calculate percentage change, and sort stocks using Heap Sort based on gain/loss. 
Implement fast searching using a Hash Map (dictionary) and compare performance with Python's built-in sorted() and normal search methods, including execution time and trade-off analysis."""

def generate_stock_data(num_stocks: int, seed: int = None) -> List[Dict[str, Union[str, float]]]:
    """Generate a list of stock data with random values."""
    if seed is not None:
        random.seed(seed)
    stocks = []
    for i in range(num_stocks):
        open_price = round(random.uniform(100.0, 500.0), 2)
        close_price = round(open_price + random.uniform(-20.0, 20.0), 2)
        pct_change = round(((close_price - open_price) / open_price) * 100, 2)
        stock = {
            "symbol": f"STK{i+1:04d}",
            "open": open_price,
            "close": close_price,
            "pct_change": pct_change
        }
        stocks.append(stock)
    return stocks
# Example usage:
stock_data = generate_stock_data(1000, seed=42)