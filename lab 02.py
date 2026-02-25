# Task 1: Statistical Summary of Survey Data
def calculate_stats(data_list):
    """
    Calculates mean, minimum, and maximum of a list.
    """
    if not data_list:
        return None
    
    mean_val = sum(data_list) / len(data_list)
    min_val = min(data_list)
    max_val = max(data_list)
    
    return mean_val, min_val, max_val

# Driver code
survey_data = [45, 22, 18, 30, 50, 27, 42]
mean, minimum, maximum = calculate_stats(survey_data)

print(f"Data: {survey_data}")
print(f"Mean: {mean:.2f}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print("-" * 20)




# Task 2: Armstrong Number Checker
def is_armstrong(number):
    # Convert to string to easily iterate digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == number

# Input from user
num = int(input("Enter a number to check Armstrong: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
print("-" * 20)




# Task 3 - Version 1: Basic Logic
def is_leap_year_basic(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    



# Task 3 - Version 2: Optimized/Pythonic
def is_leap_year_optimized(year):
    # Returns True if leap year, else False
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Testing both
year_input = int(input("Enter year for Task 3: "))
print(f"Basic Check: {is_leap_year_basic(year_input)}")
print(f"Optimized Check: {is_leap_year_optimized(year_input)}")
print("-" * 20)




# Task 4: Original "Student" Code (Verbose)
def sum_odd_even_original(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum = even_sum + num
        else:
            odd_sum = odd_sum + num
    return odd_sum, even_sum

# Task 4: AI Refactored Code (Using List Comprehensions)
def sum_odd_even_refactored(numbers):
    # More readable and concise
    even_sum = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return odd_sum, even_sum

# Test Data
my_tuple = (10, 23, 4, 7, 15, 88, 3)

original_res = sum_odd_even_original(my_tuple)
refactored_res = sum_odd_even_refactored(my_tuple)

print(f"Tuple: {my_tuple}")
print(f"Original Result (Odd, Even): {original_res}")
print(f"Refactored Result (Odd, Even): {refactored_res}")