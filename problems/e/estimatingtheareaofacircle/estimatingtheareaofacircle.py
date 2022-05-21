#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import pi

def main():

    while True:
        r, m, c = [float(val) for val in input().split()]

        if r == m == c == 0:
            break

        true_area = pi * r ** 2
        estimated_area = (r * 2) ** 2 * c / m

        print(true_area, estimated_area)



if __name__ == '__main__':
    main()