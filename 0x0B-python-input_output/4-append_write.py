#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8)
    """
    with open(filename, mode='a', encoding='utf-8') as myfile:
        num_char = myfile.write(text)
        return num_char
