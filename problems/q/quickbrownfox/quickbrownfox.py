#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
import string


def main():
    n = int(input())
    for _ in range(n):
        phrase = input().lower()
        missing = [char for char in string.ascii_lowercase]

        for letter in phrase:
            if letter in missing:
                missing.remove(letter)

        if missing:
            print("missing", "".join(missing))

        else:
            print('pangram')


if __name__ == '__main__':
    main()