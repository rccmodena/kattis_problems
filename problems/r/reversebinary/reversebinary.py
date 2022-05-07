#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    print(int(bin(n)[::-1][:-2], 2))


if __name__ == '__main__':
    main()