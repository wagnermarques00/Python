# Creating a dictionary named 'contacts' with nested dictionaries as values.
contacts = {
    "joseph@mail.com": {"name": "joseph", "phone": "1111-2222"},
    "jotaro@mail.com": {"name": "jotaro", "phone": "3333-4444"},
    "luffy@mail.com": {"name": "luffy", "phone": "5555-6666"},
    "ichigo@mail.com": {"name": "ichigo", "phone": "7777-8888"},
}

# Creating a copy of the 'contacts' dictionary named 'copied_contacts'.
copied_contacts = contacts.copy()

# Modifying the value of a specific key in the 'copied_contacts' dictionary.
copied_contacts["luffy@mail.com"] = {"name": "Luffy Gear 5"}

# Displaying the original and modified values associated with the key "luffy@mail.com"
print(contacts["luffy@mail.com"])  # {'name': 'luffy', 'phone': '5555-6666'}
print(copied_contacts["luffy@mail.com"])  # {'name': 'Luffy Gear 5'}
