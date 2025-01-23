#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if not (isinstance(dividend, (int, float))
                    and isinstance(divisor, (int, float))):
                raise TypeError
            division = dividend / divisor
            result.append(division)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
