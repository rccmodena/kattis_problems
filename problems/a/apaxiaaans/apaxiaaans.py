#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

from asyncore import compact_traceback

def main():
    name = input()
    compact_name = ""
    for i in range(len(name)):
        if i == 0:
            compact_name += name[i]
        else:
            if name[i - 1] != name[i]:
                compact_name += name[i]
    print(compact_name)

    
if __name__ == '__main__':
    main()