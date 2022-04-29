#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for _ in range(n):
        list_strips = [int(val) for val in input().split()]
        sum_strips = sum(list_strips[1:])
        print(sum_strips - (list_strips[0] - 1))

if __name__ == '__main__':
    main()