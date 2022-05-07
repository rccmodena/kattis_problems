#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    hand = input().split()
    count_k = dict()
    for card in hand:
        if count_k.get(card[0]) is None:
            count_k[card[0]] = 1
        else:
            count_k[card[0]] += 1
    print(max(count_k.values()))

if __name__ == "__main__":
    main()