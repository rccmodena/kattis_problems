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

        dict_items = dict()        
        for _ in range(n):
            line = input().split()
            name = line[0]
            for item in line[1:]:
                if dict_items.get(item) is None:
                    dict_items[item] = [name]
                else:
                    dict_items[item].append(name)

        for item in sorted(dict_items.keys()):
            print(item, *sorted(dict_items[item]))
        print("")

if __name__ == '__main__':
    main()