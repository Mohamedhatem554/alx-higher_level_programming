#!/usr/bin/python3

def add_args(argv):
    n = len(argv) - 1
    if n == 0:
        print("{}".format(n))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
        print("{}".format(add))


if __name__ == "__main__":
    import sys
    add_args(sys.argv)
