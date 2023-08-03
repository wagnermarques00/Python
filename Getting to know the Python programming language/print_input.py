name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(name, age)  # Wagner 32
print(name, age, end="...\n")  # Wagner 32...
print("Name:", name, ", Age:", age)  # Name: Wagner , Age: 32
print(f"Name: {name}, Age: {age}")  # Name: Wagner , Age: 32
