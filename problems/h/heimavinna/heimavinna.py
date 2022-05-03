#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    problems = input().split(';')
    total_problems = 0
    for item in problems:
        if '-' in item:
            interval = [int(val) for val in item.split('-')]
            total_problems += len([x for x in range(interval[0], interval[1] + 1)])
        else:
            total_problems +=1

    print(total_problems)


if __name__ == '__main__':
    main()