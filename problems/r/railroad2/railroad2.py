#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    x, y = [int(val) for val in input().split()]

    if y % 2 == 0:
        print("possible")
    else:
        print("impossible")


if __name__ == '__main__':
    main()