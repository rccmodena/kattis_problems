#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    _ = int(input())

    numbers = [int(val) for val in input().split()]
    print(sum(numbers))

if __name__ == '__main__':
    main()