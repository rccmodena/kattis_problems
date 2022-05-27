#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    while True:
        n = int(input())
        if n == 0:
            break

        list_original = [int(input()) for _ in range(n)]
        list_1 = sorted(list_original)
        list_2 = sorted([int(input()) for _ in range(n)])

        for val in list_original:
            print(list_2[list_1.index(val)])
        print("")


if __name__ == '__main__':
    main()