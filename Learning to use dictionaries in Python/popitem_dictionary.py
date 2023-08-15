# Creating a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Using the popitem() method to remove and return an arbitrary key-value pair.
print(contacts.popitem())  # ('ichigo@mail.com', {'name': 'ichigo', 'phone': '7777-8888'})
print(contacts.popitem())  # ('luffy@mail.com', {'name': 'luffy', 'phone': '5555-6666'})
print(contacts.popitem())  # ('jotaro@mail.com', {'name': 'jotaro', 'phone': '3333-4444'})
print(contacts.popitem())  # ('joseph@mail.com', {'name': 'joseph', 'phone': '1111-2222'})

# The dictionary is now empty, and using popitem() again will result in an error.
# print(contacts.popitem())  # Error
