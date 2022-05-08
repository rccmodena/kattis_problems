#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
import operator
from functools import reduce

def main():
    n, h, v = [int(val) for val in input().split()]

    volume = [4]
    if h > n - h:
        volume.append(h)
    else:
        volume.append(n - h)

    if v > n - v:
        volume.append(v)
    else:
        volume.append(n - v)

    print(reduce(operator.mul, volume, 1))


if __name__ == '__main__':
    main()