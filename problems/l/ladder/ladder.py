#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import ceil, sin, radians


def main():
    h, v = [int(val) for val in input().split()]

    print(ceil(h / sin(radians(v))))

if __name__ == '__main__':
    main()