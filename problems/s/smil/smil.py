#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    memory = input()

    position = 0
    eyes = False
    for i, letter in enumerate(memory):
        if letter == ':' or letter == ';':
            position = i
            eyes = True
        else:
            if eyes:
                if letter == ')':
                    print(position)
                    eyes = False
                elif letter != '-':
                    eyes = False


if __name__ == '__main__':
    main()