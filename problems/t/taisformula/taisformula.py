#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def calc_area(x1, x2, y1, y2):
    return (y1 + y2) / 2 * (x2 - x1) / 1000


def main():
    n = int(input())

    prev_x = 0
    prev_y = 0
    volume = 0
    for i in range(n):
        x, y = [float(val) for val in input().split()]
        if i != 0:
            volume += calc_area(prev_x, x, prev_y, y)

        prev_x = x
        prev_y = y

    print(volume)


if __name__ == '__main__':
    main()