#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    s, t, n = [int(val) for val in input().split()]
    d = [int(val) for val in input().split()]
    b = [int(val) for val in input().split()]
    c = [int(val) for val in input().split()]

    total_time = s
    for i in range(n):
        total_time += d[i]
        if total_time % c[i] != 0:
            total_time += c[i] - (total_time % c[i])
        total_time += b[i]
    
    total_time += d[n]

    if total_time <= t:
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()