# Task 1: Student Class
class Student:
    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch

    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")

# Creating an object and testing
student1 = Student("Sai Suraj", "23CS001", "CSE")
student1.display_details()




# Task 2: Multiples of a Number (For vs While Loop)

def print_multiples_for(n):
    print(f"\nMultiples of {n} (Using For Loop):")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def print_multiples_while(n):
    print(f"\nMultiples of {n} (Using While Loop):")
    count = 1
    while count <= 10:
        print(f"{n} x {count} = {n * count}")
        count += 1

# Testing
number = int(input("\nEnter a number for Task 2: "))
print_multiples_for(number)
print_multiples_while(number)





# Task 3: Age Classification

def classify_age(age):
    if age < 0:
        return "Invalid Age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Testing
try:
    age_input = int(input("\nEnter age for Task 3: "))
    print(f"Category: {classify_age(age_input)}")
except ValueError:
    print("Please enter a valid number.")





  
# Task 4: Sum of First n Numbers (3 Approaches)

def sum_for_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_while_loop(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_formula(n):
    # Mathematical Formula: n(n+1)/2
    return (n * (n + 1)) // 2

# Testing
n_val = int(input("\nEnter n for Sum calculation (Task 4): "))
print(f"Sum (For Loop): {sum_for_loop(n_val)}")
print(f"Sum (While Loop): {sum_while_loop(n_val)}")
print(f"Sum (Formula): {sum_formula(n_val)}")




# Task 5: Bank Account Class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current Balance for {self.account_holder}: ${self.balance}")

# Testing
my_account = BankAccount("Suraj", 1000)
my_account.check_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(2000) # Testing insufficient funds





