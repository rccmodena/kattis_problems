#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    cpr = [int(val) for val in input() if val.isdigit()]
    list_values = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
    cpr_sum = sum([a * b for a, b in zip(cpr, list_values)])
    if cpr_sum % 11 == 0:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()