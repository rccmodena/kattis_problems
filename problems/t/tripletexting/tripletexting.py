#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    s = input()
    n = len(s)
    n_word = n // 3

    words = [s[i:i + n_word] for i in range(0, n, n_word)]

    if words[0] == words[1]:
        print(words[0])
    elif words[0] == words[2]:
        print(words[0])
    else:
        print(words[1])


if __name__ == '__main__':
    main()