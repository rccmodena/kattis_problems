#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    t = int(input())

    for i in range(t):
        r, c = [int(val) for val in input().split()]
        image = list()
        for row in range(r):
            image.append(input())
        print(f"Test {i + 1}")
        for row in range(r - 1, -1, -1):
            print(image[row][::-1])


if __name__ == '__main__':
    main()