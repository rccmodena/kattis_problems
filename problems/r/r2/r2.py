#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    r1, s = [int(x) for x in input().split()]
    r2 = 2 * s - r1
    print(r2)

if __name__ == '__main__':
    main()