#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        new_dict = a_dictionary.copy()
        del new_dict[key]
        return new_dict
    return a_dictionary
