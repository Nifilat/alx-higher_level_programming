#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_it_int = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        is_it_int = False
    return is_it_int
