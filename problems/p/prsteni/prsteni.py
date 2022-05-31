#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def simplify_frac(a, b):

    if a == b:
        return 1, 1
    elif a == 1 or b == 1:
        return a, b

    else:
        min_val = min(a, b)
        divisor = 2
        while divisor <= min_val:
            if a % divisor == 0 and b % divisor == 0:
                a /= divisor
                b /= divisor
            else:
                divisor += 1
        return int(a), int(b)


def main():
    n = int(input())
    rings = [int(val) for val in input().split()]
    first_ring = rings[0]
    for ring in rings[1:]:
        a, b = simplify_frac(first_ring, ring)
        print(f"{a}/{b}")

if __name__ == '__main__':
    main()