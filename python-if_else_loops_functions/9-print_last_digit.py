#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, str):
        raise TypeError("Error")
    else:
        number_str = str(number)
        print("{}".format(number_str[-1:]), end='')
        return number_str[-1:]
