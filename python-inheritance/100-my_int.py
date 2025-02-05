#!/usr/bin/python3


class MyInt(int):
    """
    MyInt is a rebel class that inverts == and != operators
    """
    
    def __eq__(self, other):
        """
        Invert the behavior of the equality operator
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Invert the behavior of the inequality operator
        """
        return not super().__ne__(other)
