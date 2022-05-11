#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    result = []
    for i in range(1, 6):
        blimp = input()
        if "FBI" in blimp:
            result.append(i)
    if result:
        print(*result)
    else:
        print("HE GOT AWAY!")
        

if __name__ == '__main__':
    main()