#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
import math

def get_t(x1, v0, ang):
    return x1 / (v0 * math.cos(math.radians(ang)))


def get_y1(v0, t, ang):
    g = 9.81
    return v0 * t * math.sin(math.radians(ang)) - 0.5 * g * (t ** 2)


def main():
    n = int(input())

    for _ in range(n):
        v0, ang, x1, h1, h2 = [float(val) for val in input().split()]

        t = get_t(x1, v0, ang)
        y1 = get_y1(v0, t, ang)

        if (y1 >= (h1 + 1)) and (y1 <= (h2 - 1)):
            print("Safe")
        else:
            print("Not Safe")


if __name__ == '__main__':
    main()