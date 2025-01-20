#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    suma = 0

    for i in args:
        suma += int(i)
    print("{}".format(suma))


if __name__ == "__main__":
    main()
