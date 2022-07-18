#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import sqrt

def calc_distance(x1, y1, x2, y2):
    b = x2 - x1
    c = y2 - y1
    return sqrt((b ** 2) + (c ** 2))


def main():
    x, y, x1, y1, x2, y2 = [int(val) for val in input().split()]

    if x > min(x1, x2) and x < max(x1, x2):
        if y > max(y1, y2):
            print(calc_distance(x, y, x, max(y1, y2)))
        else:
            print(calc_distance(x, y, x, min(y1, y2)))

    elif y > min(y1, y2) and y < max(y1, y2):
        if x > max(x1, x2):
            print(calc_distance(x, y, max(x1, x2), y))
        else:
            print(calc_distance(x, y, min(x1, x2), y ))

    else:
        list_corners = [calc_distance(x, y, x1, y1)]

        list_corners.append(calc_distance(x, y, x2, y2))

        x3 = x1
        y3 = y2
        list_corners.append(calc_distance(x, y, x3, y3))

        x4 = x2
        y4 = y1
        list_corners.append(calc_distance(x, y, x4, y4))

        print(min(list_corners))


if __name__ == '__main__':
    main()