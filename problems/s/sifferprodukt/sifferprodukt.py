#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    x = input().split()
    while True:
        total = 1
        for digit in x:
            int_digit = int(digit)
            if int_digit > 0:
                total *= int_digit
        if total < 10:
            break
        else:
            x = str(total)
    print(total)


if __name__ == '__main__':
    main()