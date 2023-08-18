salary = 2000


def bonus_salary(bonus):
    """
    Adds a bonus to the global salary variable and returns the new salary.

    Parameters:
    bonus (int): The bonus amount to be added to the salary.

    Returns:
    int: The new salary after adding the bonus.
    """
    global salary
    salary += bonus
    return salary


# Calling the bonus_salary function and printing the resulting salary with bonus.
salary_with_bonus = bonus_salary(500)
print(salary_with_bonus)  # 2500
