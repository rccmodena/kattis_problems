#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    x = 0
    n = int(input())
    for _ in range(n):
        # Read number
        n = input()

        # Determine number and power
        number = int(n[:-1])
        power = int(n[-1:])

        # Calculate result
        x += number ** power

    print(x)


if __name__ == '__main__':
    main()