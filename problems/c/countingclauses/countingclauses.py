#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    m, n = [int(val) for val in input().split()]

    for _ in range(m):
        _ = input()

    if m >= 8:
        print("satisfactory")
    else:
        print("unsatisfactory")



if __name__ == '__main__':
    main()