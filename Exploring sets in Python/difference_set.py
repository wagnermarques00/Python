# Creating two sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}

# Finding the elements in set_a that are not in set_b.
difference_a = set_a.difference(set_b)

# Finding the elements in set_b that are not in set_a.
difference_b = set_b.difference(set_a)

print(difference_a)  # {1}
print(difference_b)  # {4}
