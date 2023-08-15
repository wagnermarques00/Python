# Creating two sets
set_a = {1, 2, 3}
set_b = {4, 1, 2, 5, 6, 3}

# Checking if set_a is a subset of set_b.
subset_a = set_a.issubset(set_b)

# Checking if set_b is a subset of set_a.
subset_b = set_b.issubset(set_a)

print(subset_a)  # True
print(subset_b)  # False
