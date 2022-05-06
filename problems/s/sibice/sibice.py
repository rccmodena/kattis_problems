#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import sqrt

def main():
    n, w, h = [int(val) for val in input().split()]

    max_length = int(sqrt(w ** 2 + h ** 2))

    for _ in range(n):
        l = int(input())

        if l <= max_length:
            print("DA")
        else:
            print("NE")


if __name__ == '__main__':
    main()