#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    list_int = []
    for _ in range(n):
        list_int.append(input())
    
    for number in list_int[::-1]:
        print(number)


if __name__ == '__main__':
    main()