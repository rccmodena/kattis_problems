#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

key_dict = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': '0'
}

def get_key_sequence(text):
    sequence = ""
    previous_key = '1'
    for letter in text:
        temp_sequence = key_dict[letter]

        if previous_key == temp_sequence[0]:
            sequence += ' '
        sequence += temp_sequence
        previous_key = sequence[-1]

    return sequence


def main():
    n = int(input())

    for i in range(n):
        text = input()
        print(f"Case #{i + 1}: {get_key_sequence(text)}")


if __name__ == '__main__':
    main()