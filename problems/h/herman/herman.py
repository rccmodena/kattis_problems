#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import pi

def calc_euclidian_area(radius):
    return pi * (radius ** 2)


def calc_taxicab_area(radius):
    return 2.0 * (radius ** 2)


def main():
    r = int(input())

    print(calc_euclidian_area(r))
    print(calc_taxicab_area(r))


if __name__ == '__main__':
    main()