#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        Public instance method area(self)
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method integer_validator(self, name, value)
        that validates value

        arguments:
            _name: string
            _value: int, if not, raise TypeError,
                if less or equal 0 ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
