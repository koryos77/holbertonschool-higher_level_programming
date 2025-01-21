#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maximum = my_list[0]
    for integer in my_list[1:]:
        if integer > maximum:
            maximum = integer
    return maximum
