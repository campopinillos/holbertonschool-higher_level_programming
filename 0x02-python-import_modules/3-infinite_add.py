#!/usr/bin/python3
import sys
sum = 0
if len(sys.argv) - 1 > 0:
    for i in range(1, len(sys.argv)):
        sum += int(str(sys.argv[i]))
print("{}".format(sum))
