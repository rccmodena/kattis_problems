#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def count_vowels(sentence):
    vowels = 0
    for letter in sentence:
        if letter.lower() in "aeiou":
            vowels += 1
    return vowels


def main():
    s = input()
    print(count_vowels(s))


if __name__ == '__main__':
    main()