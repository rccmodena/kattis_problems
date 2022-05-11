#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    cipher_text = input()
    cipher_size = len(cipher_text)
    per_times = cipher_size // 3
    new_text = "PER" * per_times
    print(sum([1 for i in range(cipher_size) if cipher_text[i] != new_text[i]]))


if __name__ == '__main__':
    main()