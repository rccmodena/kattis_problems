#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    while True:
        sum_digits = sum([int(val) for val in str(n)])

        if n % sum_digits == 0:
            print(n)
            break
        n += 1


if __name__ == '__main__':
    main()