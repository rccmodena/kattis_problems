#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a, b = input().split()
    a = int(a[::-1])
    b = int(b[::-1])
    if a > b:
        print(a)
    else:
        print(b)


if __name__ == '__main__':
    main()