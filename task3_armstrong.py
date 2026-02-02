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

