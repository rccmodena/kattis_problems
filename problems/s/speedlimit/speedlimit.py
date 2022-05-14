#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from dis import dis


def main():
    n = int(input())
    while n > 0:
        distance = 0
        previous_t = 0
        for _ in range(n):
            s, t = [int(val) for val in input().split()]
            distance += (t - previous_t) * s
            previous_t = t

        print(f"{distance} miles")
        n = int(input())


if __name__ == '__main__':
    main()