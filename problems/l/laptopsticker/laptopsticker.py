#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    wc, hc, ws, hs = [int(val) for val in input().split()]

    if (ws + 2 <= wc ) and (hs + 2 <= hc):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()