#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    alphabet_size = len(alphabet)
    while True:
        t = input()
        if t == "0":
            break
        n = int(t.split()[0])
        string = t.split()[1][::-1]
        encrypted = ""
        for letter in string:
            encrypted += alphabet[(alphabet.index(letter) + n) % alphabet_size]
        print(encrypted)
        

if __name__ == '__main__':
    main()