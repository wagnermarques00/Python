# Sets in Python do not support indexing or slicing.
# If you want to access their values, you need to convert the set to a list.

# Creating a set named "numbers" with some values.
numbers = {1, 2, 3, 2}

# Converting the set "numbers" to a list.
numbers = list(numbers)

# Printing the first element of the list "numbers"
print(numbers[0])  # 1


# Creating a set named "cars" with some car brands.
cars = {"Toyota", "Hyundai", "Toyota"}

# Iterating through the set "cars" and printing each car brand.
for car in cars:
    print(car)  # Toyota Hyundai
