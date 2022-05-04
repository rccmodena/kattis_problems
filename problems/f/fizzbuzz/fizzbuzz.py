#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    x, y, n = [int(val) for val in input().split()]

    for i in range(1, n+1):
        if (i % x == 0) and (i % y == 0):
            print("FizzBuzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    main()