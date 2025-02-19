#!/usr/bin/python3
"""
Fucntion that inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file, after each line containing a specif

    Args:
        filename (str): name of the file
        search_string (str): string to search
        new_string (stl): string to add
    """
    with open(filename,"r+") as file:
        lines = file.readline()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
