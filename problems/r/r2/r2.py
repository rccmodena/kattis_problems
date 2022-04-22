#! /usr/bin/python3

import sys

for line in sys.stdin:
    r1s = [int(x) for x in line.split()]
    r1 = r1s[0]
    s = r1s[1]
    r2 = 2 * s - r1
    print(r2)