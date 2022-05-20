#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a, b, c, d, e = [int(val) for val in input().split()]
    score = int(input())

    if score >= a:
        print("A")
    elif score >= b:
        print("B")
    elif score >= c:
        print("C")
    elif score >= d:
        print("D")
    elif score >= e:
        print("E")
    else:
        print("F")



if __name__ == '__main__':
    main()