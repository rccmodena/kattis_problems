#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    for _ in range(n):
        a, b, c = [int(val) for val in input().split()]
        if c in [a + b, a - b, b - a, a * b, a / b, b / a]:
            print("Possible")
        else:
            print("Impossible")


if __name__ == '__main__':
    main()