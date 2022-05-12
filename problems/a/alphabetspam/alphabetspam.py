#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from string import ascii_lowercase, ascii_uppercase


def main():
    string = input()
    string_size = len(string)

    ratios = [0] * 4
    for letter in string:
        if letter == '_':
            ratios[0] += 1

        elif letter in ascii_lowercase:
            ratios[1] += 1

        elif letter in ascii_uppercase:
            ratios[2] += 1

        else:
            ratios[3] += 1

    print(*[val / string_size for val in ratios], sep='\n')


if __name__ == '__main__':
    main()