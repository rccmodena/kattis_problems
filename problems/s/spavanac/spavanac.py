#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    h, m = [int(val) for val in input().split()]

    if m >= 45:
        m -= 45
    else:
        if h == 0:
            h = 23
        else:
            h -= 1

        m = 60 + (m - 45)

    print(f"{h} {m}")
        

if __name__ == '__main__':
    main()