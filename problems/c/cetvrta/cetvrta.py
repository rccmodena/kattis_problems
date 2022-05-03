#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    fourth_x = []
    fourth_y = []
    for _ in range(3):
        x, y = [int(val) for val in input().split()]
        if x in fourth_x:
            fourth_x.remove(x)
        else:
            fourth_x.append(x)

        if y in fourth_y:
            fourth_y.remove(y)
        else:
            fourth_y.append(y)

    print(fourth_x[0], fourth_y[0])


if __name__ == '__main__':
    main()