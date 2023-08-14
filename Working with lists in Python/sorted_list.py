languages = ["Python", "JS", "C", "Java", "CSharp"]

# ['C', 'JS', 'Java', 'Python', 'CSharp']
print(sorted(languages, key=lambda x: len(x)))

# ["Python", "CSharp", "Java", "JS", "C"]
print(sorted(languages, key=lambda x: len(x), reverse=True))
