#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    min_balance = 0
    balance = 0
    for _ in range(n):
        t = int(input())
        balance += t
        if balance < min_balance:
            min_balance = balance
    print(abs(min_balance))


if __name__ == '__main__':
    main()