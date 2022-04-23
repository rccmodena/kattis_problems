#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import sys

def main():
    x = None
    for line in sys.stdin:
        if x is None:
            x = int(line)
        else:
            y = int(line)
            if x > 0:
                if y > 0:
                    print('1')
                else:
                    print('4')
            else:
                if y > 0:
                    print('2')
                else:
                    print('3')
            break

if __name__ == '__main__':
    main()