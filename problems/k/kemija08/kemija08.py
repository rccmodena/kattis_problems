#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

VOWELS = "aeiou"

def main():
    sentence = input()
    decoded = ""
    skip = 0
    for letter in sentence:
        if skip > 0:
            skip -= 1
            continue

        decoded += letter
        if letter in VOWELS:
            skip = 2

    print(decoded)


if __name__ == '__main__':
    main()