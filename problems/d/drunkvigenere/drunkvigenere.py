#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from string import ascii_uppercase

def main():
    c = input()
    k = input()

    decrypted = ""
    len_upper = len(ascii_uppercase)
    for i, letter in enumerate(c):
        index_letter = ascii_uppercase.index(letter)
        index_k = ascii_uppercase.index(k[i])
        if i % 2 == 0:
            decrypted += ascii_uppercase[(index_letter - index_k) % len_upper]
        else:
            decrypted += ascii_uppercase[(index_letter + index_k) % len_upper]
    print(decrypted)


if __name__ == '__main__':
    main()