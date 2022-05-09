#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""


def main():
    n = int(input())
    x = [int(val) for val in input().split()]
    y = [int(val) for val in input().split()]
    
    for i in x:
        if i not in y:
            print(i)
            break


if __name__ == '__main__':
    main()