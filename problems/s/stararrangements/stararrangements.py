#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    s = int(input())
    print(f"{s}:")
    for first_line in range(2, s//2 + 2):
        for second_line in [first_line -1, first_line]:
            two_lines = first_line + second_line
            if s % two_lines == 0 or s % two_lines == first_line:
                print(f"{first_line},{second_line}")


if __name__ == '__main__':
    main()