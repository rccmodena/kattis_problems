#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
from math import sqrt, degrees, pi, acos

def distance_origin(x, y):
    return sqrt(x ** 2 + y ** 2)


def calc_area_triangle(r, x, y):
    triangle_side_1 = distance_origin(x, y)
    triangle_side_2 = sqrt(r ** 2 - triangle_side_1 ** 2)
    return triangle_side_1 * triangle_side_2


def calc_angle_triangle(r, x, y):
    triangle_side_1 = distance_origin(x, y)
    return 2 * degrees(acos(triangle_side_1 / r))


def area_sector(radius, angle):
    '''
    angle in degrees
    '''
    return ((angle * pi) / 360) * radius ** 2


def areas_cookies(r, x, y):
    if x == y == 0:
        return [pi * r ** 2] * 2 
    else:
        areas = list()
        area_triangle = calc_area_triangle(r, x, y)
        angle_triangle = calc_angle_triangle(r, x, y)
        areas.append(area_sector(r, 360 - angle_triangle) + area_triangle)
        areas.append(area_sector(r, angle_triangle) - area_triangle)

        return sorted(areas, reverse=True)


def main():
    while True:
        try:
            line = input()
            r, x, y = [float(val) for val in line.split()]
            if distance_origin(x, y) > r:
                print("miss")
            else:
                print(*areas_cookies(r, x, y))

        except EOFError:
            break


if __name__ == '__main__':
    main()