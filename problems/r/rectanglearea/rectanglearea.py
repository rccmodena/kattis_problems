#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    x1, y1, x2, y2 = [float(val) for val in input().split()]
    area = abs(x2 - x1) * abs(y2 - y1)

    print(round(area, 3))


if __name__ == '__main__':
    main()