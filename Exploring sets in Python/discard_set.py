# Using the discard method to remove elements from a set.

numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numbers)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing element 1 from the set.
numbers.discard(1)

# Attempting to remove non-existing element 45.
numbers.discard(45)
print(numbers)  # {0, 2, 3, 4, 5, 6, 7, 8, 9}
