#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

TOTAL_TIME = 210

def main():
    k = int(input())
    n = int(input())

    time_left = TOTAL_TIME
    for _ in range(n):
        t, z = [int(val) if i == 0 else val for i, val in enumerate(input().split())]
        
        time_left -= t
        if time_left <= 0:
            break

        if z == 'T':
            k += 1
            if k > 8:
                k = 1

    print(k)


if __name__ == '__main__':
    main()