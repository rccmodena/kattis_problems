#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    t = [int(val) for val in input().split()]
    print(len(list(filter(lambda val: val < 0, t))))

if __name__ == '__main__':
    main()