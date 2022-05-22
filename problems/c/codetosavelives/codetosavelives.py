#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    t = int(input())

    for _ in range(t):
        number_1 = int("".join(input().split()))
        number_2 = int("".join(input().split()))
        distance = number_1 + number_2
        print(" ".join([digit for digit in str(distance)]))


if __name__ == '__main__':
    main()