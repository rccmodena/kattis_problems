#! /usr/bin/python3

import sys

for line in sys.stdin:
    if int(line) % 2 == 0:
        print("Bob")
    else:
        print("Alice")
