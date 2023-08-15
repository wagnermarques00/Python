# Creating a dictionary named 'contact' with keys and values.
contact = {"name": "luffy", "phone": "5555-6666"}

# Using the setdefault() method to add a key-value pair if the key is not already present.
# In this case, since "name" is already present, its value is not changed.
contact.setdefault("name", "Naruto")
print(contact)  # {'name': 'luffy', 'phone': '5555-6666'}

# Using the setdefault() method to add a new key-value pair ("age", 18) since "age" is not present.
contact.setdefault("age", 18)
print(contact)  # {'name': 'luffy', 'phone': '5555-6666', 'age': 18}
