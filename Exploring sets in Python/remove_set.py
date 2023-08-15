# Using the remove() method to delete specific elements from a set.

numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numbers)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numbers.remove(0)  # Removing element 0 from the set.
print(numbers)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
