#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n, p, q = [int(val) for val in input().split()]

    quocient = (p + q) // n
    if quocient % 2 == 0:
        print("paul")
    else:
        print("opponent")


if __name__ == '__main__':
    main()