#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n, k = [int(val) for val in input().split()]

    x = input().split()

    print(*[x[i] for i in range(k - 1, n, k)])


if __name__ == '__main__':
    main()