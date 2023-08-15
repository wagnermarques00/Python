# A set is a collection that has no repeating objects.
# We use sets to represent mathematical sets or eliminate duplicate items from an iterable.
# A set does not provide any ordering guarantees.

# Set in a list
set_numbers = set([1, 2, 3, 1, 3, 4])
print(set_numbers)  # {1, 2, 3, 4}


# Set in a string
set_apple = set("apple")
print(set_apple)  # {'e', 'p', 'a', 'l'}


# set in a tuple
set_cars = set(
    (
        "Toyota",
        "Chevrolet",
        "Hyundai",
        "Chevrolet",
        "Toyota",
    )
)
print(set_cars)  # {'Chevrolet', 'Toyota', 'Hyundai'}

# Set using curly braces
languages = {"Python", "Java", "Python"}
print(languages)  # {'Java', 'Python'}
