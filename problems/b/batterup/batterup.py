#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    at_bats = [int(val) for val in input().split()]

    slugging_sum = 0
    for at_bat in at_bats:
        if at_bat == -1:
            n += at_bat
        else:
            slugging_sum +=at_bat

    slugging_percentage = slugging_sum/n
    print(f"{slugging_percentage:.17f}")


if __name__ == '__main__':
    main()