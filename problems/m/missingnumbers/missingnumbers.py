#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    list_numbers = list()
    for _ in range(n):
        list_numbers.append(int(input()))
    
    good_job = True
    for i in range(1, max(list_numbers)+1):
        if i not in list_numbers:
            good_job = False
            print(i)

    if good_job:
        print("good job")


if __name__ == '__main__':
    main()