#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for _ in range(n):
        command = input()
        if 'Simon says' == command[:10]:
            print(command[11:])


if __name__ == '__main__':
    main()