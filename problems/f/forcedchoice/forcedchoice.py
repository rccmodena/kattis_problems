#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n, p, s = [int(val) for val in input().split()]

    for _ in range(s):
        choices = [int(val) for val in input().split()]
        if p in choices[1:]:
            print("KEEP")
        else:
            print("REMOVE")


if __name__ == '__main__':
    main()