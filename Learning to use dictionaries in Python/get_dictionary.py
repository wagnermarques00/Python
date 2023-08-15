# Creating a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Attempting to access a non-existent key using dictionary indexing results in an error.
# print(contacts["key"])  # Error

# Using the get() method to retrieve values from the dictionary.
# The method returns None if the key is not found.
print(contacts.get("key"))  # None

# Using the get() method with a default value to retrieve values.
# The method returns an empty dictionary {} if the key is not found.
print(contacts.get("key", {}))  # {}

# Using the get() method to retrieve values for an existing key.
print(contacts.get("luffy@mail.com"))  # {'name': 'luffy', 'phone': '5555-6666'}

# Using the get() method with a default value for an existing key.
print(contacts.get("luffy@mail.com", {}))  # {'name': 'luffy', 'phone': '5555-6666'}
