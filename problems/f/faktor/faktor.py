#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a, i = [int(val) for val in input().split()]
    scientists = a * (i - 1) +1
    print(scientists)

if __name__ == '__main__':
    main()