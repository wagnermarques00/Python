# Iterating through dictionaries:

# Defining a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Iterating through 'contacts' using keys and printing each key along with its value.
for key in contacts:
    print(key, contacts[key])

# Iterating through 'contacts' using items() and printing each key along with its value.
for key, value in contacts.items():
    print(key, value)

# Output for both loops:
# joseph@mail.com {'name': 'joseph', 'phone': '1111-2222'}
# jotaro@mail.com {'name': 'jotaro', 'phone': '3333-4444'}
# luffy@mail.com {'name': 'luffy', 'phone': '5555-6666'}
# ichigo@mail.com {'name': 'ichigo', 'phone': '7777-8888'}
