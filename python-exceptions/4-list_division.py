#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for i in range(list_length):
        try:
            is_number1 = isinstance(my_list_1[i], (int, float))
            is_number2 = isinstance(my_list_2[i], (int, float))
            if is_number1 and is_number2:
                result[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            pass
        return result
