#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import math

def main():
    s = input()

    sum_characters = 0
    for letter in s:
        sum_characters += ord(letter)
    
    print(chr(math.floor(sum_characters / len(s))))


if __name__ == '__main__':
    main()