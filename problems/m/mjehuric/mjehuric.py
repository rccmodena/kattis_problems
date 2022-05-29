#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    pieces = input().split()
    correct_list = ['1', '2', '3', '4', '5']

    while True:
        if all([pieces[i] == correct_list[i] for i in range(5)]):
            break
        for i in range(4):
            if pieces[i + 1] < pieces[i]:
                pieces[i], pieces[i + 1] = pieces[i + 1], pieces[i]
                print(" ".join(pieces))


if __name__ == '__main__':
    main()