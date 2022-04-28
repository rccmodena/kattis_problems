#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for _ in range(n):
        b, p = [float(val) for val in input().split()]

        if p == 0:
            abpm_min = 0
            bpm = 0
            abpm_max = 0
        else:
            abpm = 60 / p
            bpm = 60 * b / p
            abpm_min = bpm - abpm
            abpm_max = bpm + abpm
        print(f"{abpm_min:.4f} {bpm:.4f} {abpm_max:.4f}")


if __name__ == '__main__':
    main()