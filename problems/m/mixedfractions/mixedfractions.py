#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    while True:
        n, d = [int(val) for val in input().split()]
        if n == d == 0:
            break
        else:
            whole = n // d
            n = n % d
            print(f"{whole} {n} / {d}")


if __name__ == '__main__':
    main()