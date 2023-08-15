# A dictionary is an unordered set of key:value pairs.
# Keys are unique within a dictionary instance.
# Dictionaries are defined using braces: {}.
# Dictionaries contain comma-separated key:value pairs.

# Creating a dictionary using key:value pairs.
person = {"name": "Wagner", "age": 32}

# Alternative way to create a dictionary.
person = dict(name="Wagner", age=28)
print(person)  # {'name': 'Wagner', 'age': 28}

# Adding a new key:value pair to the dictionary.
person["phone"] = "1234-5678"
print(person)  # {'name': 'Wagner', 'age': 28, 'phone': '1234-5678'}
