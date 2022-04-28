#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    c = float(input())
    l = int(input())

    cost_lawns = 0
    for _ in range(l):
        wi, li = [float(val) for val in input().split()]
        cost_lawns += wi * li * c

    print(f"{cost_lawns:.7f}")


if __name__ == '__main__':
    main()