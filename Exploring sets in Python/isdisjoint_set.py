# Creating three sets
set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8, 9}
set_c = {1, 0}

# Checking if set_a and set_b have no common elements.
disjoint_b = set_a.isdisjoint(set_b)

# Checking if set_a and set_c have no common elements.
disjoint_c = set_a.isdisjoint(set_c)

print(disjoint_b)  # True
print(disjoint_c)  # False
