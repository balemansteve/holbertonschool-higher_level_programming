#!/usr/bin/python3
def islower(c):
    char = ord(c)
    if char >= ord('a') or char >= ord('z'):
        return True
    elif char >= ord('Z') or char >= ord('Z'):
        return False
    else:
        return False
