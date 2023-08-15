# Creating a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Printing the dictionary's items using the items() method.
print(contacts.items())
# dict_items([
#   ('joseph@mail.com', {'name': 'joseph', 'phone': '1111-2222'}),
#   ('jotaro@mail.com', {'name': 'jotaro', 'phone': '3333-4444'}),
#   ('luffy@mail.com', {'name': 'luffy', 'phone': '5555-6666'}),
#   ('ichigo@mail.com', {'name': 'ichigo', 'phone': '7777-8888'})
# ])
