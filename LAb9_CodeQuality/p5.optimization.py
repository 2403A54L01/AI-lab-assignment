'''# Problem Statement 5: Performance Optimization
import time
import numpy as np # Note: requires 'pip install numpy'

def sum_of_squares_loop(numbers):
    """Slow approach using a for loop."""
    total = 0
    for num in numbers:
        total += num ** 2
    return total

def sum_of_squares_optimized(numbers):
    """Fast approach using NumPy vectorization."""
    return np.sum(np.array(numbers)**2)

# TEST WITH LARGE DATASET
data = list(range(1000000))

# TIMING COMPARISON
start = time.time()
sum_of_squares_loop(data)
print(f"Loop Time: {time.time() - start:.4f}s")

start = time.time()
sum_of_squares_optimized(data)
print(f"NumPy Time: {time.time() - start:.4f}s")

# TRADE-OFF: NumPy is much faster but requires an external library.'''

# Problem Statement 5: Performance Optimization
import time
def sum_of_squares_loop(numbers):
    """Slow approach using a for loop."""
    total = 0
    for num in numbers:
        total += num ** 2
    return total
def sum_of_squares_optimized(numbers):
    """Fast approach using list comprehension."""
    return sum(num ** 2 for num in numbers)
# TEST WITH LARGE DATASET
data = list(range(1000000))
# TIMING COMPARISON
start = time.time()
sum_of_squares_loop(data)
print(f"Loop Time: {time.time() - start:.4f}s")

start = time.time()
sum_of_squares_optimized(data)
print(f"Optimized Time: {time.time() - start:.4f}s")
# TRADE-OFF: List comprehension is faster than a for loop but may still be slower than NumPy for very large datasets.

