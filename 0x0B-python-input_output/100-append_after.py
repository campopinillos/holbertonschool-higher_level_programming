#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    text = ""
    with open(filename, encoding='utf-8') as my_file:
        for line in my_file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, mode='w', encoding='utf-8') as my_file:
        my_file.write(text)
