#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def binary_watch(digit):
    return bin(int(digit))[2:].zfill(4).replace('1', '*').replace('0', '.')


def main():
    time = input()

    hours_tens = binary_watch(time[0])
    hours_ones = binary_watch(time[1])
    minutes_tens = binary_watch(time[2])
    minutes_ones = binary_watch(time[3])

    for i in range(4):
        print(f"{hours_tens[i]} {hours_ones[i]}   {minutes_tens[i]} {minutes_ones[i]}")


if __name__ == '__main__':
    main()