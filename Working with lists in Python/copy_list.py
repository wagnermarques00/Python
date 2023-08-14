list_example = [1, "Python", [40, 30, 20]]

list_2 = list_example.copy()

print(list_example)  # [1, 'Python', [40, 30, 20]]
print(list_2)  # [1, 'Python', [40, 30, 20]]
print(id(list_2), id(list_example))  # 3180076857984 3180076759936
