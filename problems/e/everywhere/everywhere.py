#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        set_of_cities = set()
        for _ in range(n):
            set_of_cities.add(input())
        print(len(set_of_cities))


if __name__ == '__main__':
    main()