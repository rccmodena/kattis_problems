#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    y, p = input().split()

    if y[-2:] == "ex":
        print(y+p)
    elif y[-1] == 'e':
        print(y+'x'+p)
    elif y[-1] in "aiou":
        print(y[:-1]+"ex"+p)
    else:
        print(y+'ex'+p)


if __name__ == '__main__':
    main()