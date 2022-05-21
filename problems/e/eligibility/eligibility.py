#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for _ in range(n):
        name, secondary_begin, birth, courses = input().split()

        if int(secondary_begin[:4]) >= 2010:
            print(f"{name} eligible")
        elif int(birth[:4]) >= 1991:
            print(f"{name} eligible")
        elif int(courses) >= 41:
            print(f"{name} ineligible")
        else:
            print(f"{name} coach petitions")

if __name__ == '__main__':
    main()