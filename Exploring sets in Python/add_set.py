# Demonstrating the use of the add() method to add elements to a set.
prize_draw = {1, 23}  # Initial set with elements 1 and 23.

# Adding element 25 to the set.
prize_draw.add(25)
print(prize_draw)  # {1, 25, 23}

# Adding element 42 to the set.
prize_draw.add(42)
print(prize_draw)  # {1, 42, 25, 23}

# Attempting to add element 25 again.
prize_draw.add(25)
print(prize_draw)  # {1, 42, 25, 23}
