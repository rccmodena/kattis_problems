#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    free_lunch = set()
    for _ in range(n):
        s, t = [int(val) for val in input().split()]
        for day in range(s, t + 1):
            free_lunch.add(day)

    print(len(free_lunch))


if __name__ == '__main__':
    main()