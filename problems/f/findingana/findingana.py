#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    s = input()
    suffix_ini = s.index('a')
    print(s[suffix_ini:])


if __name__ == '__main__':
    main()