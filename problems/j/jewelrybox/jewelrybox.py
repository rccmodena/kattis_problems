#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
from math import sqrt


def calc_roots_derivative(X, Y):
    if X < Y:
        threshold = X / 2
    else:
        threshold = Y / 2

    a = 12
    b = (-4 * X) + (-4 * Y)
    c = X * Y
    delta = b ** 2 - 4 * a * c
    root_1 = ((- 1 * b) + sqrt(delta)) / (2 * a)
    root_2 = ((- 1 * b) - sqrt(delta)) / (2 * a)

    list_valid_roots = list()
    if (0 < root_1) and (root_1 < threshold):
        list_valid_roots.append(root_1)

    if (0 < root_2) and (root_2 < threshold):
        list_valid_roots.append(root_2)

    return list_valid_roots


def calc_volume(list_valid_roots, X, Y):
    biggest_volume = 0
    for h in list_valid_roots:
        volume = (4 * h ** 3) - (2 * X * h ** 2) - (2 * Y * h ** 2) + (X * Y * h)
        if volume > biggest_volume:
            biggest_volume = volume

    return biggest_volume


def main():
    t = int(input())

    for _ in range(t):
        X, Y = [int(val) for val in input().split()]
        list_valid_roots = calc_roots_derivative(X, Y)
        print(calc_volume(list_valid_roots, X, Y))


if __name__ == '__main__':
    main()