#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
from math import tan, pi

def calc_area_regular_polygon(n, l):
    # https://en.wikipedia.org/wiki/Regular_polygon#Area
    # A = 1/4 * n * s ** 2 * cot(pi/n)
    # n: number of sides
    # s: side lenght
    cot_term = 1 / tan(pi / n)
    return 1/4 * n * l ** 2 * cot_term

def calc_area_expansion_rectangles(n, l, d, g):
    return n * l * d * g

def calc_area_expansion_arc(n, radius, angle):
    return n * pi * radius ** 2 * (angle / 360)

def main():
    n = int(input())

    for _ in range(n):
        n, l, g, d = [int(val) for val in input().split()]
        total_area = calc_area_regular_polygon(n, l) + calc_area_expansion_rectangles(n, l, d, g) + calc_area_expansion_arc(n, (d * g), (360 / n))
        print(total_area)


if __name__ == '__main__':
    main()