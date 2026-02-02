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