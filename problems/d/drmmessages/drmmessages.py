#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from string import ascii_uppercase

def divide(message):
    half_length = len(message) // 2
    divide_list = []
    divide_list.append(message[:half_length])
    divide_list.append(message[half_length:])
    return divide_list


def rotate(divide_list):
    size_ascii = len(ascii_uppercase)
    for i, half in enumerate(divide_list):
        rotation = sum([ascii_uppercase.index(letter) for letter in half])
        divide_list[i] = "".join([ascii_uppercase[(ascii_uppercase.index(letter) + rotation) % size_ascii] for letter in half])

    return divide_list


def merge(rotate_list):
    size_ascii = len(ascii_uppercase)
    return "".join([ascii_uppercase[(ascii_uppercase.index(a) + ascii_uppercase.index(b)) % size_ascii] for a, b in zip(*rotate_list)])


def main():
    drm = input()
    divide_list = divide(drm)
    rotate_list = rotate(divide_list)
    print(merge(rotate_list))


if __name__ == '__main__':
    main()