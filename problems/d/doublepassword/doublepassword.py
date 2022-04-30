#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    s1 = input()
    s2 = input()

    sequences = 1
    for i, val in enumerate(s1):
        if val == s2[i]:
            sequences *= 1
        else:
            sequences *= 2

    print(sequences)


if __name__ == '__main__':
    main()