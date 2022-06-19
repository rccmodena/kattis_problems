#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    dictionary = dict()
    while True:
        line = input()
        if line:
            english, foreign_language = line.split()
            dictionary[foreign_language] = english
        else:
            break

    while True:
        try:
            word = input()
            if word:
                print(dictionary.get(word, "eh"))
        except EOFError:
            break
    

if __name__ == '__main__':
    main()