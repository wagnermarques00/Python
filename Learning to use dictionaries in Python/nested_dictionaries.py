# Dictionaries can store any type of Python object as a value,
# as long as the key to that value is an immutable object
# like strings and numbers.

# Defining a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Accessing and printing a specific value from the nested dictionary in 'contacts'.
print(contacts["luffy@mail.com"]["phone"])  # 5555-6666
