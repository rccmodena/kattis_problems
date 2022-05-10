#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import sqrt

def calc_semiperimeter(sides):
    '''
    Calculate the semiperimeter according to the reference:
    https://www.geeksforgeeks.org/maximum-area-quadrilateral/
    '''
    return sum(sides) / 2


def calc_bretschneiders_formula(sides):
    """
    Tip: https://www.geeksforgeeks.org/maximum-area-quadrilateral/

    Bretschneider’s formula, that is used to calculte the area of a general
    quadilateral, is given by:

    K = math.sqrt((s - a) * (s - b) * (s - c) * (s - d) - k1)
    where a, b, c, d are the sides of the quadrilateral; s is the semiperimeter;
    and k1 is:

    k1 = (a * b * c * d) * (math.cos(math.radians((ang1 + ang2) / 2)) ** 2)
    where ang1, ang2 are are two opposite angles of the quadilateral.

    Bretschneider’s formula is maximized only when the opposite angles sum to
    pi (180°), then k1 = 0.
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]
    d = sides[3]
    s = calc_semiperimeter(sides)

    return sqrt((s - a) * (s - b) * (s - c) * (s - d))


def main():
    sides = [int(val) for val in input().split()]

    print(calc_bretschneiders_formula(sides))


if __name__ == '__main__':
    main()