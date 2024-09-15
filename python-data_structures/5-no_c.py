#!/usr/bin/python3
def no_c(my_string):
    no_c = ""
    for i in my_string:
        if i == "c" or i == "C":
            break
        else:
            no_c += i
    return no_c
