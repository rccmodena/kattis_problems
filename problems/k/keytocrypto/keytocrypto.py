#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import string

def main():
    ciphertext = input()
    secret = [letter for letter in input()]
    max_length = len(string.ascii_uppercase)

    for letter in ciphertext:
        chipher_index = string.ascii_uppercase.index(letter)
        shift = string.ascii_uppercase.index(secret.pop(0))
        original_letter = string.ascii_uppercase[chipher_index - (shift % max_length)]
        secret.append(original_letter)
        print(original_letter, end="")


if __name__ == '__main__':
    main()