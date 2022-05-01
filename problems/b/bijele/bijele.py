#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    correct_set = [1, 1, 2, 2, 2, 8]
    pieces = [correct_set[i] - int(p) for i, p in enumerate(input().split())]
    print(*pieces)

if __name__ == '__main__':
    main()