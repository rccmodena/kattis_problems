#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from itertools import permutations

def main():
    x_list = [digit for digit in input()]
    x = int("".join(x_list))

    smallest =  0
    for permutation in permutations(x_list, len(x_list)):
        val = int("".join(permutation))
        if val > x:
            if (smallest == 0) or (val < smallest):
                smallest = val
    print(smallest)


if __name__ == '__main__':
    main()