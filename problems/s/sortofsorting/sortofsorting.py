#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            last_names = list()
            for i in range(n):
                last_name = input()
                short_last_name = last_name[:2] + str(i).zfill(3)
                last_names.append([last_name, short_last_name])
            last_names = sorted(last_names, key=lambda name: name[1])
            for last_name in last_names:
                print(last_name[0])
            print("")

if __name__ == '__main__':
    main()