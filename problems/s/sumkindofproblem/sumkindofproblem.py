#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""


def sum_positive_int(n):
    return sum([val for val in range(n + 1)])


def sum_odd_int(n):
    return sum([val for val in range(1, n*2, 2)])


def sum_even_int(n):
    return sum([val for val in range(2, n*2+1, 2)])


def main():
    p = int(input())

    for _ in range(p):
        k, n = [int(val) for val in input().split()]
        print(f"{k} {sum_positive_int(n)} {sum_odd_int(n)} {sum_even_int(n)}")


if __name__ == '__main__':
    main()