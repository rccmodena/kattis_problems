#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import radians, sin, cos

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        x = 0
        y = 0
        correct_angle = 90
        for _ in range(m):
            angle, distance = [float(val) for val in input().split()]
            correct_angle += angle
            x += cos(radians(correct_angle)) * distance
            y += sin(radians(correct_angle)) * distance
        print(x, y)


if __name__ == '__main__':
    main()