#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    Function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding='utf-8') as myfile:
        line_num = 0
        for line in myfile:
            line_num += 1
        myfile.seek(0)
        if (line_num <= nb_lines) or (nb_lines <= 0):
            print(myfile.read(), end="")
        else:
            line_num = 0
            while line_num < nb_lines:
                print(myfile.readline(), end="")
                line_num += 1
