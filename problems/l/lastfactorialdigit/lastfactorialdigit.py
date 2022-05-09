#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import factorial

def main():
    n = int(input())

    for _ in range(n):
        t = int(input())
        print(str(factorial(t))[-1])


if __name__ == '__main__':
    main()