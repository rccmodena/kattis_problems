#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    initial_number = None
    for _ in range(n):
        if initial_number is None:
            initial_number = int(input())
        else:
            val = int(input())
            if val % initial_number == 0:
                print(val)
                initial_number = None


if __name__ == '__main__':
    main()