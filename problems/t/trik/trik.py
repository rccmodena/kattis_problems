#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    ball = 1
    for move in input():
        if move == 'A':
            if ball == 1:
                ball = 2
            elif ball == 2:
                ball = 1
        elif move == 'B':
            if ball == 2:
                ball = 3
            elif ball == 3:
                ball = 2
        else:
            if ball == 3:
                ball = 1
            elif ball == 1:
                ball = 3
    print(ball)

if __name__ == '__main__':
    main()