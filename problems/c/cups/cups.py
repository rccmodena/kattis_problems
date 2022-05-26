#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    size_color = dict()
    for _ in range(n):
        cr = input().split()
        try:
            c = cr[0]
            r = int(cr[1])
        except:
            c = cr[1]
            r = float(int(cr[0])/2)
        size_color[r] = c

    for size in sorted(size_color.keys()):
        print(size_color[size])

if __name__ == '__main__':
    main()