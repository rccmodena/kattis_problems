#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    for _ in range(int(input())):
        stops = int(input())
        current_number_passengers = 0
        for _ in range(stops):
            current_number_passengers = (current_number_passengers + 0.5) * 2

        print(int(current_number_passengers))


if __name__ == '__main__':
    main()