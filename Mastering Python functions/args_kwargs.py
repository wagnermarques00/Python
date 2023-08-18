def print_poem(full_date, *args, **kwargs):
    """
    Prints a poem with its text, metadata, and full date.

    Parameters:
    full_date (str): The full date of the poem.
    *args (tuple): Variable positional arguments containing the poem's text lines.
    **kwargs (dict): Variable keyword arguments containing metadata related to the poem.
    """
    text = "\n".join(args)
    meta_data = "\n".join([f"{key.title()}: {value}" for key, value in kwargs.items()])
    message = f"{full_date}\n\n{text}\n\n{meta_data}"

    print(message)


# Calling the function with provided poem text and metadata
print_poem("Zen of Python", "Beautiful is better than ugly.", author="Tim Peters", year=1999)

# Output:
# Zen of Python
#
# Beautiful is better than ugly.
#
# Author: Tim Peters
# Year: 1999
