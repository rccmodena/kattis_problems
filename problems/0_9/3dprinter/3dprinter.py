#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
from math import ceil

def main():
    n = int(input())

    min_days = n

    for days_printer in range(2, n):
        printers = 2 ** (days_printer - 1)
        days = ceil(n / printers) + (days_printer - 1)
        if days <= min_days:
            min_days = days
        else:
            break;

    print(min_days)


if __name__ == '__main__':
    main()