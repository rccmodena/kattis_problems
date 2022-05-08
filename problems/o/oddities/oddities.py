#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    for _ in range(n):
        x = int(input())
        if x % 2 == 0:
            print(f"{x} is even")
        else:
            print(f"{x} is odd")


if __name__ == '__main__':
    main()