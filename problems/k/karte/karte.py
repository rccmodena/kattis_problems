#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

CARD_LENGHT = 3

def main():
    deck = input()

    all_cards = {
        'P': [],
        'K': [],
        'H': [],
        'T': []
    }

    cards = [deck[i:i + CARD_LENGHT] for i in range(0, len(deck), CARD_LENGHT)]

    duplicate = False
    for card in cards:
        t = card[0]
        xy = int(card[1:])
        if xy in all_cards[t]:
            duplicate = True
            break
        all_cards[t].append(xy)

    if duplicate:
        print("GRESKA")
    else:
        print(*[13 - len(cards) for cards in all_cards.values()])


if __name__ == '__main__':
    main()