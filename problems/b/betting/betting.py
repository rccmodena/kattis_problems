#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a = int(input())
    option_one = a / 100.0
    option_two = (100 - a) / 100.0
    if option_one == 0:
        print(f"{option_one:.10f}")
    else:
        print(f"{(1 / option_one):.10f}")

    if option_two == 0:
        print(f"{option_two:.10f}")
    else:
        print(f"{(1 / option_two):.10f}")


if __name__ == '__main__':
    main()