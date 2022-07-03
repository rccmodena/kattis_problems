#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a, b = input().split()
    size_a = len(a)
    size_b = len(b)

    index_letter_a = 0
    index_letter_b = 0
    for i, letter in enumerate(a):
        index_letter_a = i
        index_letter_b = b.find(letter)
        if index_letter_b != -1:
            break

    for i, letter_b in enumerate(b):
        for j, letter_a in enumerate(a):
            if i == index_letter_b:
                print(a, end="")
                break
            if j == index_letter_a:
                print(letter_b, end="")
            else:
                print(".",end="")
        print("")

if __name__ == '__main__':
    main()