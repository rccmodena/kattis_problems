#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    list_days = [int(val) for val in input().split()]

    list_days.sort(reverse=True)
    
    total_days = 0
    for i, days in enumerate(list_days):
        days_grown = i + days + 2
        if total_days < days_grown:
            total_days = days_grown

    print(total_days)

if __name__ == '__main__':
    main()