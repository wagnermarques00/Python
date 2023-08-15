# Creating a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Using the values() method to retrieve the dictionary's values as an iterable object.
print(contacts.values())
# dict_values([
#     {'name': 'joseph', 'phone': '1111-2222'},
#     {'name': 'jotaro', 'phone': '3333-4444'},
#     {'name': 'luffy', 'phone': '5555-6666'},
#     {'name': 'ichigo', 'phone': '7777-8888'}
# ])
