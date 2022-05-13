#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a, b, c = [int(val) for val in input().split()]
    space_1 = b - a
    space_2 = c - b
    if space_1 > space_2:
        print(space_1 - 1)
    else:
        print(space_2 - 1)

if __name__ == '__main__':
    main()