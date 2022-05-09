#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    l, r = [int(val) for val in input().split()]
    if l == 0 and r == 0:
        print("Not a moose")
    elif l != r:
        print(f"Odd {max([l, r]) * 2}")
    else:
        print(f"Even {l + r}")


if __name__ == '__main__':
    main()