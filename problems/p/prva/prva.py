#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""


def main():
    r, c = [int(val) for val in input().split()]

    list_words = list()
    list_vertical = ["" for _ in range(c)]
    for _ in range(r):
        line = input()
        for word in line.split("#"):
            if len(word) < 2:
                continue
            list_words.append(word)
        for i, char in enumerate(line):
            list_vertical[i] += char

    for line in list_vertical:
        for word in line.split("#"):
            if len(word) < 2:
                continue
            list_words.append(word)
    
    print(sorted(list_words)[0])


if __name__ == '__main__':
    main()