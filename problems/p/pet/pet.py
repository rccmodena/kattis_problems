#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    winner = [0, 0]
    for i in range(5):
        grade = sum([int(val) for val in input().split()])
        if winner[1] < grade:
            winner[0] = i + 1
            winner[1] = grade
    print(f"{winner[0]} {winner[1]}")


if __name__ == '__main__':
    main()