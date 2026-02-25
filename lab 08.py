#Task Description #1 (Password Strength Validator – Apply AI in Security Context)
import re       
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@$!%*?&]', password):
        return False
    if ' ' in password:
        return False
    return True

# AI-generated test cases
assert is_strong_password("Abcd@123") == True
assert is_strong_password("abcd123") == False
assert is_strong_password("Abcdefgh@1234") == True
assert is_strong_password("Abcdefg") == False
assert is_strong_password("Abcdefg1") == False
assert is_strong_password("Abcdefg@") == False
assert is_strong_password("Abcdefg 1@") == False
assert is_strong_password("Abcdefg1@") == True
print("All test cases passed!")




#Task Description #2 (Number Classification with Loops)
def classify_number(n):
    if n is None or isinstance(n, str):
        return "Invalid input"
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
# AI-generated test cases
assert classify_number(10) == "Positive"
assert classify_number(-5) == "Negative"
assert classify_number(0) == "Zero"
assert classify_number("abc") == "Invalid input"
assert classify_number(None) == "Invalid input"
assert classify_number(-1) == "Negative"
assert classify_number(1) == "Positive"
print("All test cases passed!") 




#Task Description #3 (Anagram Checker)
import re
def is_anagram(str1, str2):
    def clean_string(s):
        return re.sub(r'[\W_]+', '', s).lower()
    return sorted(clean_string(str1)) == sorted(clean_string(str2))
# AI-generated test cases
assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("Dormitory", "Dirty Room") == True
assert is_anagram("", "") == True
assert is_anagram("abc", "abc") == True
assert is_anagram("abc", "def") == False    
print("All test cases passed!")



#Task Description #4 (Inventory Class)
class Inventory:
    def __init__(self):
        self.stock = {}
    def add_item(self, name, quantity):
        if name in self.stock:
            self.stock[name] += quantity
        else:
            self.stock[name] = quantity
    def remove_item(self, name, quantity):
        if name in self.stock and self.stock[name] >= quantity:
            self.stock[name] -= quantity
        else:
            raise ValueError("Not enough stock to remove")
    def get_stock(self, name):
        return self.stock.get(name, 0)
# AI-generated test cases
inv = Inventory()
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10
inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5
inv.add_item("Notebook", 20)
assert inv.get_stock("Notebook") == 20
try:
    inv.remove_item("Pen", 10)
except ValueError as e:
    assert str(e) == "Not enough stock to remove"
print("All test cases passed!")



