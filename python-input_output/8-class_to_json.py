#!/usr/bin/python3
"""Module for reading a text file"""
import json


def class_to_json(obj):
    """
    Function that returns the dict description with simple data struct
    for a JSON serialization of an object

    Arguments:
        obj: Instance of a class

    Returns:
        Dictionary description with simple data structure
    """
    dictionary = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (str, int, bool, list, dict)):
            dictionary[key] = value
    return dictionary
