#!/usr/bin/python3
"""
print_square module
Function that prints a square with the character #.

"""


def print_square(size):
    """
    Function that prints a square with the character #.
    Args:
        size (int): First input.
    Raise: TypeError
    Return: A square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("\n".join(["".join(["#" for i in range(size)])
                    for j in range(size)]))
