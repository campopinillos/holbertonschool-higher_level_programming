#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operation = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if operator in list(operation.keys()):
        print("{} {} {} = {}".format(a, operator, b,
                                     operation[operator](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
