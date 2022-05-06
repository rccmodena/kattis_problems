#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    w = int(input())
    n = int(input())

    area = 0
    for _ in range(n):
        wi, li = [int(val) for val in input().split()]
        area += wi * li
    print(area//w)


if __name__ == '__main__':
    main()