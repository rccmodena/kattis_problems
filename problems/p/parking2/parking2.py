#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    t = int(input())
    for _ in range(t):
        t = int(input())
        x = [int(val) for val in input().split()]
        min_x = min(x)
        max_x = max(x)
        delta_x = max_x - min_x
        park = delta_x // 2
        print(delta_x + (park - min_x) + (max_x - park))


if __name__ == '__main__':
    main()