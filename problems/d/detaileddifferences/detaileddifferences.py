#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for _ in range(n):
        first_str = input()
        second_str = input()
        str_size = len(first_str)
        print(first_str)
        print(second_str)
        print("".join(["." if first_str[i] == second_str[i] else "*" for i in range(str_size)]) + "\n")


if __name__ == '__main__':
    main()