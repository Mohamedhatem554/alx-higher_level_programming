#!/usr/bin/python3

def print_arg(argv):
    n = len(argv) - 1
    if len == 0:
        print("{} arguments.".format(n))
        return
    else:
        if len == 1:
            print("{} argument:".format(n))
        else:
            print("{} arguments:".format(n))

        x = 1
        while x <= n:
            print("{:d}: {:s}".format(x, argv[x]))
            x += 1


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
