#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    r, c, zr, zc = [int(val) for val in input().split()]

    matrix = [input() for _ in range(r)]

    for line in matrix:
        new_line = "".join([char * zc for char in line])
        for i in range(zr):
            print(new_line)


if __name__ == '__main__':
    main()