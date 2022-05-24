#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import pi


def calc_area_circle(radius):
    return pi * (radius ** 2)


def main():
    r, c = [int(val) for val in input().split()]

    total_area = calc_area_circle(r)
    total_cheese = calc_area_circle(r - c)
    percent_cheese  = total_cheese / total_area * 100

    print(percent_cheese)


if __name__ == '__main__':
    main()