# Creating a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Creating a dictionary using the fromkeys() method.
# The keys are given in a list, and the values are set to None by default.
first_dict = dict.fromkeys(["name", "phone"])

# Creating another dictionary using the fromkeys() method.
# This time, default values are set to "empty".
second_dict = dict.fromkeys(["name", "phone"], "empty")

print(first_dict)  # Output: {'name': None, 'phone': None}
print(second_dict)  # Output: {'name': 'empty', 'phone': 'empty'}
