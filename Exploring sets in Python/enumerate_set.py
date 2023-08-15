# Sometimes it's necessary to know the index of the object inside the for loop.
# For this, we can use the enumerate function.

# Set of car brand names.
cars = {"Toyota", "Hyundai", "Chevrolet"}

# Iterate through the set "cars" using enumerate to get index and car brand.
for index, car in enumerate(cars):
    print(f"{index}: {car}")
    # 0: Toyota
    # 1: Hyundai
    # 2: Chevrolet
