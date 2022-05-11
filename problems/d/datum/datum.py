#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import datetime

dow = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def main():
    d, m = [int(val) for val in input().split()]
    print(dow[datetime.datetime(2009, m, d, 0, 30).weekday()])


if __name__ == '__main__':
    main()