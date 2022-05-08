#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    phrase = input().split()
    if len(set(phrase)) == len(phrase):
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()