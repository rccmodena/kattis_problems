#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    dominant = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
    not_dominant = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}

    nb = input().split()
    n = int(nb[0]) * 4
    b = nb[1]
    points = 0

    for _ in range(n):
        card = input().replace('\n','')
        if card[1] == b:
            points += dominant[card[0]]
        else:
            points += not_dominant[card[0]]

    print(points)


if __name__ == '__main__':
    main()