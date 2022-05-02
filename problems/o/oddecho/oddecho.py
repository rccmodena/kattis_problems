#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for i in range(n):
        word = input()
        if i % 2 == 0:
            print(word)


if __name__ == '__main__':
    main()