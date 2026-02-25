#task1_weatherimport requests

def get_weather(city):
    # SECURITY RISK: API Key is hardcoded and visible!
    api_key = "12345_SECRET_KEY" 
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()

print(get_weather("Hyderabad"))

import os

def get_weather_secure(city):
    # SECURE: Fetches key from environment variables
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("No API Key found")
    
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()




#task2_security
def save_user(name, email, password):
    with open("users.txt", "a") as f:
        # RISK: Storing password in plain text
        f.write(f"{name},{email},{password}\n")

save_user("Suraj", "suraj@example.com", "password123")

import hashlib

def save_user_secure(name, email, password):
    # SECURE: Hash the password before storing
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    
    with open("users_secure.txt", "a") as f:
        f.write(f"{name},{email},{hashed_pw}\n")

save_user_secure("Suraj", "suraj@example.com", "password123")




#task3_armstrong
def is_armstrong(number):
    # Convert number to string to easily count digits
    num_str = str(number)
    
    # Get the number of digits (power to raise to)
    power = len(num_str)
    
    # Calculate sum: take each digit, convert to int, raise to power
    total = sum(int(digit) ** power for digit in num_str)
    
    # Check if the calculated total equals the original number
    return total == number

# Example Usage
print(is_armstrong(153))  # Output: True




#task4_sorting
def bubble_sort(arr):
    n = len(arr)
    # Outer loop for number of passes
    for i in range(n):
        # Inner loop to compare adjacent elements
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Logic: Moves larger elements to the end one by one (like bubbles rising).
# Efficiency: O(n^2) - Very slow for large lists.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()  # Pick a pivot element
        # Create list of items greater than pivot
        items_greater = [item for item in arr if item > pivot]
        # Create list of items lower than pivot
        items_lower = [item for item in arr if item <= pivot]
        
        # Recursively sort both lists and combine
        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
# Logic: Divide and conquer. Splits array into smaller sub-arrays based on a pivot.
# Efficiency: O(n log n) - Much faster for large data.




#task5_recommendation
# A simple product database with categories
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics"},
    {"id": 2, "name": "Python Book", "category": "Books"},
    {"id": 3, "name": "Wireless Mouse", "category": "Electronics"}
]

def recommend_products(user_interest):
    recommendations = []
    
    for item in products:
        if item["category"] == user_interest:
            # Adding the "Why" reasoning
            reason = f"Because you are interested in {user_interest}"
            recommendations.append({"product": item["name"], "reason": reason})
            
    return recommendations

# User likes Electronics
print(recommend_products("Electronics"))





