#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
from math import sqrt


def main():
    l, r = [int(val) for val in input().split()]

    min_radius = sqrt(l ** 2 + l ** 2)

    if r * 2 > min_radius:
        print("fits")
    else:
        print("nope")


if __name__ == '__main__':
    main()