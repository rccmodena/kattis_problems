#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    if n % 2 == 0:
        aux_t = 0
        sum_t = 0
        for i in range(n):
            t = int(input())
            if i % 2 == 0:
                aux_t = t
            else:
                sum_t += t - aux_t
        print(sum_t)
    else:
        for i in range(n):
            t = int(input())
        print("still running")


if __name__ == '__main__':
    main()