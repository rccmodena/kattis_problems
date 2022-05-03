#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    side = 1
    height = 0
    while (n >= (side**2)):
        n -= side ** 2
        side += 2
        height += 1
    print(height)

if __name__ == '__main__':
    main()