#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    l = int(input())
    d = int(input())
    x = int(input())

    n = 0
    for val in range(l, d+1):
        if x == sum([int(digit) for digit in str(val)]):
            n = val
            break
    print(n)
    
    m = 0
    for val in range(l, d+1):
        if x == sum([int(digit) for digit in str(val)]):
            m = val

    print(m)


if __name__ == '__main__':
    main()