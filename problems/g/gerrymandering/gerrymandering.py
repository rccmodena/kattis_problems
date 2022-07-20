#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    p, d = [int(val) for val in input().split()]

    dict_votes = dict()
    for i in range(d):
        dict_votes[i + 1] = {'A': 0, 'B': 0}

    for _ in range(p):
        di, ai, bi = [int(val) for val in input().split()]
        dict_votes[di]['A'] += ai
        dict_votes[di]['B'] += bi

    total_votes = 0
    total_wa = 0
    total_wb = 0

    for i in range(d):
        a = dict_votes[i + 1]['A'] 
        b = dict_votes[i + 1]['B']
        total_votes += a + b
        win = ((a + b) // 2 ) + 1
        if a > b:
            wa = a - win
            wb = b
            print(f"A {wa} {wb}")
        else:
            wa = a
            wb = b - win
            print(f"B {wa} {wb}")
        total_wa += wa
        total_wb += wb

    e = abs(total_wa - total_wb)/ (total_votes)
    print(e)


if __name__ == '__main__':
    main()