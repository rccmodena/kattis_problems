#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    while True:
        sweet, sour = [int(val) for val in input().split()]
        if sweet == 0 and sour == 0:
            break;

        if sweet == sour:
            print("Undecided.")
        elif sweet + sour == 13:
            print("Never speak again.")
        elif sweet > sour:
            print("To the convention.")
        else:
            print("Left beehind.")


if __name__ == '__main__':
    main()