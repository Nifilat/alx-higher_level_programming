#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        var = fct(*args)
        return var
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
