#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n, q = [int(val) for val in input().split()]

    dict_companies = dict()
    for i, val in enumerate(input().split()):
        dict_companies[i + 1] = int(val)
    
    for _ in range(q):
        requests = [int(val) for val in input().split()]

        if requests[0] == 1:
            dict_companies[requests[1]] = requests[2]
        else:
            distance = abs(dict_companies[requests[1]] - dict_companies[requests[2]])
            print(distance)


if __name__ == '__main__':
    main()