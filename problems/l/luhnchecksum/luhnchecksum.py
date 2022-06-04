#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def luhn_checksum(string_digits):
    total = 0
    for i, digit in enumerate(string_digits[::-1]):
        if i % 2 == 1:
            val = int(digit) * 2
            if val > 9:
                total += int(str(val)[0]) + int(str(val)[1])
            else:
                total += val
        else:
            total += int(digit)

    if total % 10 == 0:
        return "PASS"
    else:
        return "FAIL"


def main():
    t = int(input())

    for _ in range(t):
        string_digits = input()
        print(luhn_checksum(string_digits))


if __name__ == '__main__':
    main()