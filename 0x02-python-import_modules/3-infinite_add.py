#!/usr/bin/python3

def add_args(argv):
    n = len(argv) - 1
    if n == 0:
        print("{}".format(n))
        return
    else:
        if n == 1:
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
