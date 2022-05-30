#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    k = int(input())

    count_ab = {'A':1, 'B':0}
    for _ in range(k):
        count_ab['A'], count_ab['B'] = count_ab['B'], count_ab['A'] + count_ab['B']
    print(count_ab['A'], count_ab['B'])


if __name__ == '__main__':
    main()