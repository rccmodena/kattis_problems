#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from math import sqrt

def main():
    n = int(input())
    for _ in range(n):
        message = input()
        side = int(sqrt(len(message)))
        original = ""
        for i in reversed(range(side)):
            for j in range(side):
                original += message[i + j * side]
        
        print(original)


if __name__ == '__main__':
    main()