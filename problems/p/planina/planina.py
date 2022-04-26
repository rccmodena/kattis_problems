#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    # Start with 2, and then add powers of 2
    points = 2
    for power in range(n):
        points += (2 ** power)

    print((points ** 2))


if __name__ == '__main__':
    main()