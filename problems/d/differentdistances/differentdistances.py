#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def calc_p_norm(x1, y1, x2, y2, p):
    return (abs(x1 - x2) ** p + abs(y1 - y2) ** p) ** (1/p)


def main():
    while True:
        line = input().split()

        if len(line) == 1:
            break
        print(calc_p_norm(*[float(val) for val in line]))


if __name__ == '__main__':
    main()