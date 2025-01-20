#!/usr/bin/python3
import sys


def main():

    args = sys.argv[1:]
    number_args = len(args)

    if number_args == 0:
        print("{} arguments.".format(number_args))
    elif number_args == 1:
        print("{} argument:".format(number_args))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments:".format(number_args))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
