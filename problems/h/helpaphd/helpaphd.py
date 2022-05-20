#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    for _ in range(n):
        problem = input()
        if problem == "P=NP":
            print("skipped")
        else:
            a, b = [int(val) for val in problem.split("+")]
            print(a + b)


if __name__ == '__main__':
    main()