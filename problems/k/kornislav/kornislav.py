#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    steps = sorted([int(val) for val in input().split()])

    # To create a rectangle, use the two larger number as parallel sides and the two smaller to be the other sides.
    # The area of the biggest rectangle should be the smallest side x the smallest of the bigger sides.
    print(steps[0] * steps[2])


if __name__ == '__main__':
    main()