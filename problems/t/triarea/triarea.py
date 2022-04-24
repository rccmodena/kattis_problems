#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a, b = [int(x) for x in input().split()]
    triangle_area = (a * b) / 2
    print(triangle_area)

if __name__ == '__main__':
    main()