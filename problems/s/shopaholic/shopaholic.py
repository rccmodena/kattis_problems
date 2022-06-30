#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""


def main():
    n = int(input())

    prices = sorted([int(val) for val in input().split()], reverse=True)
    max_discount = sum([val for i, val in enumerate(prices) if i % 3 == 2])

    print(max_discount)


if __name__ == '__main__':
    main()