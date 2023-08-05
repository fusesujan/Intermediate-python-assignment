## Doc String

A docstring is a special type of string used to document functions, classes, modules, or methods. It provides a way to describe what the code does, its purpose, usage, and any relevant details. Docstrings are used for documentation purposes and serve as a helpful reference for developers who use or maintain the code.

Docstrings are enclosed in triple quotes (''' or """) and are placed immediately below the definition of a function, class, or module.

<pre>
def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two input numbers.
    """
    return a + b

</pre>

To access the docstring of a function, class, or module, you can use the .**doc** attribute:

<pre>
print(add_numbers.__doc__)
</pre>
