#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
from math import sqrt


def main():
    area = int(input())
    fence_length = sqrt(area) * 4

    print(fence_length)


if __name__ == '__main__':
    main()