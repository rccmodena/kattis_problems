#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    p = int(input())

    for _ in range(p):
        k, b, n = [int(val) for val in input().split()]

        digits = []
        while n > 0:
            modulus = n % b
            digits.append(modulus)
            n = n // b
        ssd = sum([val ** 2 for val in digits])
        print(f"{k} {ssd}")


if __name__ == '__main__':
    main()