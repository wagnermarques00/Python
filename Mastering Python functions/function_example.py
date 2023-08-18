def show_message():
    """Prints a simple 'Hello world' message."""
    print("Hello world")


def show_message_2(name):
    """
    Prints a welcome message with the provided name.

    Parameters:
    name (str): The name to include in the welcome message.
    """
    print(f"Welcome {name}!")


def show_message_3(name="Anonymous"):
    """
    Prints a welcome message with the provided name or "Anonymous" if no name is given.

    Parameters:
    name (str, optional): The name to include in the welcome message. Defaults to "Anonymous".
    """
    print(f"Welcome {name}!")


# Calling the functions with various arguments and no arguments.
show_message()  # Hello world
show_message_2("Wagner")  # Welcome Wagner!
show_message_3()  # Welcome Anonymous!
show_message_3(name="Joseph")  # Welcome Joseph!
