#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    r, n = [int(val) for val in input().split()]

    reserved_rooms = list()
    for _ in range(n):
        reserved_rooms.append(int(input()))

    if r == n:
        print("too late")
    else:
        for i in range(1, r + 1):
            if i not in reserved_rooms:
                print(i)
                break


if __name__ == '__main__':
    main()