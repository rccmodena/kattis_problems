#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n, x, y = [int(val) for val in input().split()]

    for _ in range(n):
        portion = int(input())
        single_portion = portion / x
        print(int(single_portion * y))


if __name__ == '__main__':
    main()