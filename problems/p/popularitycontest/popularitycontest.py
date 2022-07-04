#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n, m = [int(val) for val in input().split()]

    popularity_factors = dict()
    for i in range(n):
        popularity_factors[i+1] = 0

    for _ in range(m):
        a, b = [int(val) for val in input().split()]
        popularity_factors[a] += 1
        popularity_factors[b] += 1

    print(*[v - k for k, v in popularity_factors.items()])


if __name__ == '__main__':
    main()
    