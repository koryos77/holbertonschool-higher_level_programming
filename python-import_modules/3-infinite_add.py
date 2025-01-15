#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args_sum = 0

    for arg in sys.argv[1:]:
        args_sum += int(arg)

    print(args_sum)
