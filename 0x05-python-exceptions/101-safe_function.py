#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)

    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
    return func
