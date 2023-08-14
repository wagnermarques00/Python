cars = ["Ford", "Chevrolet", "Toyota"]

# Ford
# Chevrolet
# Toyota
for car in cars:
    print(car)

# 0: Ford
# 1: Chevrolet
# 2: Toyota
for index, car in enumerate(cars):
    print(f"{index}: {car}")
