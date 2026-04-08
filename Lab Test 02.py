'''Task 01
"Write a Python function validate_email(email) that checks if a string is a valid email. It must contain '@' and '.', cannot start or end with special characters, and MUST end with either '.com', '.org', or '.edu'. Then, generate 10 assert test cases covering valid emails, missing TLDs, unsupported TLDs, and multiple dots to verify the function."'''


import re

def validate_email(email):
    # 1. Restrict valid domains to .com, .org, and .edu only
    allowed_tlds = ('.com', '.org', '.edu')
    if not email.endswith(allowed_tlds):
        return False
    
    # 2. Logic to block: 
    # - Starting/ending with special chars
    # - Consecutive dots (.. is not allowed)
    # - Must have @ and .
    if ".." in email:
        return False
        
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    return False

# --- Assert Test Cases ---
assert validate_email("user@example.com") == True        # Valid .com
assert validate_email("info@charity.org") == True        # Valid .org
assert validate_email("student@uni.edu") == True         # Valid .edu
assert validate_email("user@site.net") == False          # Invalid TLD (.net)
assert validate_email("@example.com") == False           # Starts with special char
assert validate_email("user@com") == False               # Missing dot/TLD
assert validate_email("user.name@site.com") == True      # Multiple dots in name (Valid)
assert validate_email("user@site..com") == False         # Multiple dots in domain (Invalid)
assert validate_email("user#@site.com") == False         # Special char check
assert validate_email("user@site.") == False             # Ends with special char

print("All Task 1 tests passed!")





'''Task 02
"Create a Python class CircularQueue using modular arithmetic for O(1) operations. Include enqueue(), dequeue(), front(), rear(), and is_full() methods. Add a dynamic resizing capability to double the capacity when the queue is full to ensure optimal space utilization."'''


class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def _resize(self):
        # Dynamic Resizing: Double the capacity
        old_queue = self.queue
        old_capacity = self.capacity
        self.capacity *= 2
        self.queue = [None] * self.capacity
        
        # Re-align elements to the new array
        for i in range(old_capacity):
            self.queue[i] = old_queue[(self.head + i) % old_capacity]
        
        self.head = 0
        self.tail = old_capacity - 1

    def enqueue(self, data):
        if self.is_full():
            self._resize()
        
        if self.is_empty():
            self.head = 0
        
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = data

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        
        data = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return data

    def front(self):
        return self.queue[self.head] if not self.is_empty() else None

    def rear(self):
        return self.queue[self.tail] if not self.is_empty() else None

# Execution/Test
cq = CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40) # This triggers dynamic resize
print(f"Front: {cq.front()}, Rear: {cq.rear()}")
print(f"Dequeued: {cq.dequeue()}")



