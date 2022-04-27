#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from re import L


def main():
    n = int(input())

    length = 0
    for _ in range(n):
        l = int(input())
        length += l

    print(length - (n - 1))


if __name__ == '__main__':
    main()