#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""


def main():
    word = input()
    permutation = input()

    drawing_components = 10

    for letter in permutation:
        if letter in word:
            word = word.replace(letter, "")
            if len(word) == 0:
                print("WIN")
                break                

        else:
            drawing_components -= 1
            if drawing_components == 0:
                print("LOSE")
                break


if __name__ == '__main__':
    main()