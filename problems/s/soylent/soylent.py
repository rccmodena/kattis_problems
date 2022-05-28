#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import ceil

CALORIES_PER_BOTTLE = 400

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ceil(n / CALORIES_PER_BOTTLE))

if __name__ == '__main__':
    main()