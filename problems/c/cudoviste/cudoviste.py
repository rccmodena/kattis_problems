#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def get_map(r, c):
    map = []
    for _ in range(r):
        map.append(input())
    return map


def has_building(park):
    return '#' in park


def n_cars(park):
    return park.count("X")


def get_park(r, c, map):
    park = []
    for i in range(r, r + 2):
        for j in range(c, c + 2):
            park.append(map[i][j])
    return park


def get_n_squashes_park(r, c, map):
    n_squashes_park = [0, 0, 0, 0, 0]
    for i in range(r - 1):
        for j in range(c - 1):
            park = get_park(i, j, map)
            if not has_building(park):
                n_squashes_park[n_cars(park)] += 1

    return n_squashes_park


def main():
    r, c = [int(val) for val in input().split()]
    map = get_map(r, c)
    n_squashes_park = get_n_squashes_park(r, c, map)
    for n in n_squashes_park:
        print(n)


if __name__ == '__main__':
    main()