#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    p, n = [int(val) for val in input().split()]

    list_boat_parts = []
    for _ in range(n):
        list_boat_parts.append(input())

    end_day = 0
    set_boat_parts = set()
    for day, part in enumerate(list_boat_parts):
        set_boat_parts.add(part)

        if len(set_boat_parts) == p:
            end_day = day + 1
            break

    if end_day == 0:
        print("paradox avoided")
    else:
        print(end_day)

if __name__ == '__main__':
    main()