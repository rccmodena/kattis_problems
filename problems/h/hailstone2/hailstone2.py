#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    n_hailstone_sequence = 1
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3*n + 1
        n_hailstone_sequence += 1

    print(n_hailstone_sequence)


if __name__ == '__main__':
    main()