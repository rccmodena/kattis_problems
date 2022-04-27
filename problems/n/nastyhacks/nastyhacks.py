#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    for _ in range(n):
        r, e, c = [int(val) for val in input().split()]
        
        if r == (e - c):
            print('does not matter')
        else:
            if r > (e - c):
                print('do not advertise')
            else:
                print('advertise')

if __name__ == '__main__':
    main()