#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    g, s, c = [int(val) for val in input().split()]

    total = (g * 3) + (s * 2) + (c * 1)

    victory = None
    if total >= 8:
        victory = 'Province'
    elif total >= 5:
        victory = 'Duchy'
    elif total >= 2:
        victory = 'Estate'

    treasure = 'Copper'
    if total >= 6:
        treasure = 'Gold'
    elif total >= 3:
        treasure = 'Silver'
    if victory == None:
        print(treasure)
    else:
        print(f'{victory} or {treasure}')


if __name__ == '__main__':
    main()