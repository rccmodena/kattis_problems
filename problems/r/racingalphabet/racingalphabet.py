#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import math

CIRCLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
TIME_ONE_LETTER = (math.pi * 60) / 28 / 15


def shortest_path(letter_1, letter_2):
    diff = abs(letter_1 - letter_2)
    if diff > len(CIRCLE) // 2 :
        return len(CIRCLE) - diff
    return diff

def main():
    n = int(input())

    for _ in range(n):
        aphorism = input()

        total_time = 0
        last_letter = None
        for letter in aphorism:
            letter_index = CIRCLE.index(letter) + 1
            if last_letter is not None:
                total_time += shortest_path(letter_index, last_letter)

            last_letter = letter_index

        total_time = total_time * TIME_ONE_LETTER + len(aphorism)

        print(round(total_time, 10))
           

if __name__ == '__main__':
    main()