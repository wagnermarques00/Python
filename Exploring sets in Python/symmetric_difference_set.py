# Creating two sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}

# Finding the elements that are in either set_a or set_b, but not in both.
symmetric_set = set_a.symmetric_difference(set_b)

print(symmetric_set)  # Output: {1, 4}
