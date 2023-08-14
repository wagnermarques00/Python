languages = ["Python", "JS", "C", "Java", "CSharp"]

languages.sort()
print(languages)  # ['C', 'CSharp', 'JS', 'Java', 'Python']

languages = ["Python", "JS", "C", "Java", "CSharp"]
languages.sort(reverse=True)
print(languages)  # ['Python', 'Java', 'JS', 'CSharp', 'C']

languages = ["Python", "JS", "C", "Java", "CSharp"]
languages.sort(key=lambda x: len(x))
print(languages)  # ['C', 'JS', 'Java', 'Python', 'CSharp']

languages = ["Python", "JS", "C", "Java", "CSharp"]
languages.sort(key=lambda x: len(x), reverse=True)
print(languages)  # ['Python', 'CSharp', 'Java', 'JS', 'C']
