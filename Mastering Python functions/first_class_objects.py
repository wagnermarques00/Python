def sum_values(a, b):
    return a + b


def subtract_values(a, b):
    return a - b


def print_result(a, b, function):
    """
    Prints the result of a binary operation performed by a given function.

    Parameters:
    a (int): The first operand.
    b (int): The second operand.
    function (function): The operation function to be applied to a and b.
    """
    result = function(a, b)
    print(f"The operation result is: {result}")


# Calling the print_result function with various operations and displaying the results.
print_result(10, 10, sum_values)  # The operation result is: 20
print_result(10, 10, subtract_values)  # The operation result is: 0

# Assigning the sum function to a variable op and calling it with arguments.
op = sum_values
print(op(1, 23))  # 24
