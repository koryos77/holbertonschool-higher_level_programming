#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args_count = len(sys.argv) - 1

    if args_count == 0:
        print("0 arguments.")
    else:
        if args_count == 1:
            print("1 argument:")
        else:
            print(f"{args_count} arguments:")

    for i in range(1, args_count + 1):
        print(f"{i}: {sys.argv[i]}")
