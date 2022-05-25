#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def sum_digits(value):
    return sum([int(val) for val in str(value)])


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        p = 11
        while True:
            if sum_digits(n) == sum_digits(n * p):
                print(p)
                break
            p += 1


if __name__ == '__main__':
    main()