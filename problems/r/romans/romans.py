#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    x = float(input())
    roman = x * 1000 * 5280/4854
    print(round(roman))


if __name__ == '__main__':
    main()