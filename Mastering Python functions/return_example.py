def calculate_total(numbers):
    """
    Calculates the sum of a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    int: The sum of the input numbers.
    """
    return sum(numbers)


def return_predecessor_and_successor(number):
    """
    Returns the predecessor and successor of a given number.

    Parameters:
    number (int): The input number.

    Returns:
    A tuple containing the predecessor and successor of the input number.
    """
    predecessor = number - 1
    successor = number + 1

    return predecessor, successor


# Calling the functions with various arguments and displaying the results.
print(calculate_total([10, 20, 34]))  # Output: 64
print(return_predecessor_and_successor(10))  # Output: (9, 11)
