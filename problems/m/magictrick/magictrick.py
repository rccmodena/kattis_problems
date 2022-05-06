#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    s = input()

    for card in s:
        if s.count(card) != 1:
            print(0)
            break
    else:
        print(1)


if __name__ == '__main__':
    main()