languages = ["Python", "JS", "C", "Java", "CSharp"]

languages.pop()
print(languages)  # ['Python', 'JS', 'C', 'Java']

languages.pop()
print(languages)  # ['Python', 'JS', 'C']

languages.pop()
print(languages)  # ['Python', 'JS']

languages.pop(0)
print(languages)  # ['JS']
