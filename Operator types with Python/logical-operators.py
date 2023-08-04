balance = 1000
withdraw = 200
limit = 100

# And
print(balance >= withdraw and withdraw <= limit)  # False

# Or
print(balance >= withdraw or withdraw <= limit)  # True

# Not
print(not balance >= withdraw)  # False
