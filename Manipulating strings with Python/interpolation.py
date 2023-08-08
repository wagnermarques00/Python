age: int = 32
language: str = "Python"
name: str = "Wagner"
PI = 3.14159
profession: str = "Developer"

# Name: Wagner. Age: 32. Profession: Developer. Language: Python

# Format
print("Name: {}. Age: {}. Profession: {}. Language: {}.".format(name, age, profession, language))

# Format
print("Name: {3}. Age: {2}. Profession: {1}. Language: {0}.".format(language, profession, age, name))

# Format
print("Name: {name}. Age: {age}. Profession: {profession}. Language: {language}.".format(name=name, age=age,
                                                                                         profession=profession, language=language))

# F String
print(f"Name: {name}. Age: {age}. Profession: {profession}. Language: {language}.")

# F String
print(f"PI value: {PI:.2f}")  # 3.14

# F String
print(f"PI value: {PI:10.2f}")  # PI value:       3.14
