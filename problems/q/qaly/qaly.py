#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    qaly = 0

    for i in range(n):
        q, y = [float(val) for val in input().split()]
        qaly += q * y

    print(f'{qaly:.3f}')

if __name__ == '__main__':
    main()