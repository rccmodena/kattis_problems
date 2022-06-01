#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for teste_case in range(n):
        g = int(input())
        list_codes_guests = list()
        for c in [int(val) for val in input().split()]:
            if c in list_codes_guests:
                list_codes_guests.remove(c)
            else:
                list_codes_guests.append(c)
        print(f"Case #{teste_case + 1}: {list_codes_guests[0]}")

if __name__ == '__main__':
    main()