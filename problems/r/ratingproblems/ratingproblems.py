#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n, k = [int(val) for val in input().split()]

    ratings = 0
    for _ in range(k):
        ratings += int(input())

    min_rating = (ratings + (-3 * (n - k))) / n
    max_rating = (ratings + (3 * (n - k))) / n
    print(min_rating, max_rating)


if __name__ == '__main__':
    main()