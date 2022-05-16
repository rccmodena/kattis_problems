#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    order = [1] * n

    for i, val in enumerate(input().split()):
        order[int(val) + 1] = i + 2
    
    print(*order)


if __name__ == '__main__':
    main()