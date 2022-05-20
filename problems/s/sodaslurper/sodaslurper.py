#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    e, f, c = [int(val) for val in input().split()]
    remaining_bottles = e + f
    soda_drinked = 0
    while remaining_bottles >= c:
        soda_bought = remaining_bottles // c
        soda_drinked += soda_bought
        remaining_bottles = (remaining_bottles % c) + soda_bought

    print(soda_drinked)

if __name__ == '__main__':
    main()