#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    while True:
        try:
            a, b = [int(val) for val in input().split()]
            print(abs(a - b))
        except EOFError:
            break


if __name__ == '__main__':
    main()