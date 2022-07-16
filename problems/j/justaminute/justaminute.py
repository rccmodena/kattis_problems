#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    sum_minutes = 0
    sum_seconds = 0
    for _ in range(n):
        m, s = [int(val) for val in input().split()]
        sum_minutes += m
        sum_seconds += s

    average_value = sum_seconds / (sum_minutes * 60) 
    if round(average_value, 8) <= 1:
        print("measurement error")
    else:
        print(average_value)


if __name__ == '__main__':
    main()