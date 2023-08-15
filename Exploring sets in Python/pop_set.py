# Using the pop() method to remove and return elements from a set.

# Creating a set
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numbers)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing the first element
numbers.pop()

# Removing the firs element (again)
numbers.pop()
print(numbers)  # Output: {2, 3, 4, 5, 6, 7, 8, 9}
