#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    s = input()
    number_e = s.count('e')
    reply_e = "e" * (number_e * 2)
    print("h" + reply_e + "y")


if __name__ == '__main__':
    main()