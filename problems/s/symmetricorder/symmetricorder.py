#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    set_number = 1
    while True:
        n = int(input())
        if n == 0:
            break

        list_names = [] 
        for _ in range(n):
            list_names.append(input())
        
        print(f"SET {set_number}")

        for i in range(0, n, 2):
            print(list_names[i])

        max_odd = n - 2 if (n - 1) % 2 == 0 else n - 1
        for i in range(max_odd, 0, -2):
            print(list_names[i])

        set_number += 1


if __name__ == '__main__':
    main()