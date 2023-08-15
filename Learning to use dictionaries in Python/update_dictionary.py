# Creating a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Using the update() method to modify or add key-value pairs in the dictionary.
contacts.update({"luffy@mail.com": {"name": "Luffy - Gear 5"}})
print(contacts["luffy@mail.com"])  # {'name': 'Luffy - Gear 5'}

contacts.update({"ichigo@mail.com": {"name": "Kurosaki Ichigo", "phone": "111-000"}})
print(contacts["ichigo@mail.com"])  # {'name': 'Kurosaki Ichigo', 'phone': '111-000'}
