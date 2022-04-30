#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    long = input().split('-')

    short = ''
    for name in long:
        short += name[0]

    print(short)


if __name__ == '__main__':
    main()