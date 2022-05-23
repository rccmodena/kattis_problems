#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import floor

def main():
    n = int(input())
    m = int(input())

    for i in range(n):
        teams = floor(0.5 + m / (n - i))
        print('*' * teams)
        m -= teams


if __name__ == '__main__':
    main()