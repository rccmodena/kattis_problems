#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for _ in range(n):
        gnomes = [int(val) for val in input().split()]
        previous_gnome = gnomes[1]
        for i in range(2, len(gnomes)):
            if gnomes[i] != previous_gnome + 1:
                print(i)
                break
            previous_gnome = gnomes[i]


if __name__ == '__main__':
    main()