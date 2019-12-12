#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    n = len(sys.argv) - 1
    operator = {"+": add, "-": sub, "*": mul, "/": div}

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(int(sys.argv[1]),
                                 sys.argv[2],
                                 int(sys.argv[1]),
                                 operator[sys.argv[2]](int(sys.argv[1]),
                                                       int(sys.argv[3]))))
