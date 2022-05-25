#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import string


def get_letter(pos):
    return string.ascii_lowercase[pos]


def get_letter_pos(letter):
    return string.ascii_lowercase.index(letter)


def get_diff(letter_original, letter_cipher):
    original_pos = get_letter_pos(letter_original)
    cipher_pos = get_letter_pos(letter_cipher)

    if original_pos <= cipher_pos:
        return cipher_pos - original_pos
    else:
        return 26 - original_pos + cipher_pos

def main():
    n, m = [int(val) for val in input().split()]

    letters = input()[::-1]
    ciphertext = input()[::-1]

    for i, cipher in enumerate(ciphertext[:-n]):
        diff = get_diff(letters[i], cipher)
        letters += get_letter(diff)

    print(letters[::-1])


if __name__ == '__main__':
    main()