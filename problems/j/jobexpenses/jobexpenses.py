#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    k = [int(val) for val in input().split() if int(val) < 0]
    print(abs(sum(k)))


if __name__ == '__main__':
    main()