#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a, b = [int(val) for val in input().split()]
    if a > b:
        print(f'{b} {a}')
    else:
        print(f'{a} {b}')


if __name__ == '__main__':
    main()