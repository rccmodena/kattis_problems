#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def base_coordinates(num):
    if num == "0":
        return (0, 0)
    elif num == "1":
        return (1, 0)
    elif num == "2":
        return (0, 1)
    else:
        return (1, 1)

def main():
    s = input()

    zoom = len(s)
    x = 0
    y = 0
    for i, digit in enumerate(s):
        exponent = zoom - (i + 1)
        x_base, y_base = base_coordinates(digit)
        if exponent == 0:
            x += x_base
            y += y_base
        else:
            x += x_base * 2 ** exponent
            y += y_base * 2 ** exponent

    print(zoom, x, y)


if __name__ == '__main__':
    main()