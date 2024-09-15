#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_inverted = my_list[::-1]
    for number in list_inverted:
        print("{:d}".format(number))
