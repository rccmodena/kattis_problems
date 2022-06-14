#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    list_names = list()
    for _ in range(n):
        list_names.append(input())

    increasing_list = sorted(list_names)
    decreasing_list = sorted(list_names, reverse=True)

    if list_names == increasing_list:
        print("INCREASING")

    elif list_names == decreasing_list:
        print("DECREASING")

    else:
        print("NEITHER")


if __name__ == '__main__':
    main()