#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = None
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if max_value is None or i > max_value:
                max_value = i
        return max_value
