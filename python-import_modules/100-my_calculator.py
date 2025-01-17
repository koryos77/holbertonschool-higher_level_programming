#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    import sys

    args_count = len(sys.argv) - 1
    if args_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    result = operators[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
