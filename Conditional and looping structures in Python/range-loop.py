# Range
# range(stop) -> range object
# range(start, stop[, step]) -> range object

loop_range = list(range(4))
print(loop_range)  # [0, 1, 2, 3]


# Range with for
for number in range(0, 11):
    print(number, end=" ")  # 0 1 2 3 4 5 6 7 8 9 10

print()

for number in range(0, 51, 5):  # Displaying the table of 5
    print(number, end=" ")  # 0 5 10 15 20 25 30 35 40 45 50
