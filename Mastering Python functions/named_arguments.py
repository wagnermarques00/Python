def saved_car_message(brand, model, year, plate):
    """
    Prints a confirmation message that a car has been saved in the database.

    Parameters:
    brand (str): The brand of the car.
    model (str): The model of the car.
    year (int): The manufacturing year of the car.
    plate (str): The license plate of the car.
    """
    print(f"Car saved to database! {brand} - {model} - {year} - {plate}")


# Different ways to call the function with various argument passing styles
saved_car_message("Fiat", "Palio", 1999, "ABC-1234")
# Car saved to database! Fiat - Palio - 1999 - ABC-1234
saved_car_message(
    brand="Fiat", model="Palio", year=1999, plate="ABC-1234"
)  # Car saved to database! Fiat - Palio - 1999 - ABC-1234
saved_car_message(
    **{"brand": "Fiat", "model": "Palio", "year": 1999, "plate": "ABC-1234"}
)  # Car saved to database! Fiat - Palio - 1999 - ABC-1234
