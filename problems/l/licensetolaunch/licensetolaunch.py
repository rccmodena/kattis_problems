#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    junk = [int(val) for val in input().split()]

    min_junk = min(junk)

    print(junk.index(min_junk))


if __name__ == '__main__':
    main()