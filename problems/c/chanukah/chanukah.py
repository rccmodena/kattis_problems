#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    p = int(input())
    for _ in range(p):
        k, n = [int(val) for val in input().split()]

        candles = [candle + 1 for candle in range(1, n + 1)]
        print(k, sum(candles))


if __name__ == '__main__':
    main()