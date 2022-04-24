#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    x = int(input())
    n = int(input())

    internet = x
    for _ in range(n):
        p = (int(input()))
        internet += (x - p)

    print(internet)

if __name__ == '__main__':
    main()