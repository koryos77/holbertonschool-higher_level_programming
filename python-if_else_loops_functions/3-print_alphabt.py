#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format(chr(i) if i not in [101, 113] else ""), end="")
