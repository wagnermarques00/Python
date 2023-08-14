# Creates a list named "fruits" with three strings
fruits = ["orange", "apple", "grape"]
print(fruits)  # ['orange', 'apple', 'grape']

# Replaces the previous list with an empty list, removing the previous elements
fruits = []
print(fruits)  # []

# Creates a list named "letters" with individual characters
letters = list("python")
print(letters)  # ['p', 'y', 't', 'h', 'o', 'n']

# Creates a list named "numbers" with numbers from 0 to 9 (range(10))
numbers = list(range(10))
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creates a list named "car" with a mix of strings, numbers, and a boolean
car = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(car)  # ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]


# Negative indices
fruits = ["apple", "orange", "grape", "pear"]
print(fruits[-1])  # pear
print(fruits[-3])  # orange
