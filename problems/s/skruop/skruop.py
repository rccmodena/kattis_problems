#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    volume = 7
    for _ in range(n):
        request = input()
        if request == "Skru op!" and volume < 10:
            volume += 1
        elif request == "Skru ned!" and volume > 0:
            volume -= 1

    print(volume)


if __name__ == '__main__':
    main()