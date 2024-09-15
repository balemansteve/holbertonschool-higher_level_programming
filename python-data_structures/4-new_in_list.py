#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list_copy
    else:
        my_list_copy.pop(idx)
        my_list_copy.insert(idx, element)
        return my_list_copy
