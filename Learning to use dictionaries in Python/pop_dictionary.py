# Creating a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Using the pop() method to remove and return the value associated with a specified key.
print(contacts.pop("joseph@mail.com"))  # Output: {'name': 'joseph', 'phone': '1111-2222'}

# Using the pop() method with a default value to handle a non-existent key.
print(contacts.pop("joseph@mail.com", {}))  # Output: {}

# Note: The key "joseph@mail.com" is already removed in the first pop() call.
