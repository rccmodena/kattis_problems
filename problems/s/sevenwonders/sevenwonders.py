#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    cards = input()

    count_cards = {
        'T': 0,
        'C': 0,
        'G': 0,
    }
    for card in cards:
        count_cards[card] += 1

    total = 0
    for value in count_cards.values():
        total += value ** 2

    total += 7 * min(count_cards.values())

    print(total)


if __name__ == '__main__':
    main()