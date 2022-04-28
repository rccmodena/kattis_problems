#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    g, t, n = [int(val) for val in input().split()]
    towing = g - t
    towing_90 = int(towing * 0.9)
    w = sum([int(val) for val in input().split()])
    print(towing_90 - w)


if __name__ == '__main__':
    main()