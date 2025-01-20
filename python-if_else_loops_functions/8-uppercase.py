#!/usr/bin/python3
def uppercase(str):
    mayuscula_str = ""
    for i in str:
        unicode_i = ord(i)
        if 97 <= unicode_i <= 122:
            unicode_i -= 32
            caracter_i = chr(unicode_i)
            mayuscula_str += caracter_i
        else:
            mayuscula_str += i
    print("{}".format(mayuscula_str))
