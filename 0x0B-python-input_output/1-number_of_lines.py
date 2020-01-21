#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding='utf-8') as myfile:
        line_num = 0
        line = myfile.readline()
        while line:
            line = myfile.readline()
            line_num += 1
        return line_num
