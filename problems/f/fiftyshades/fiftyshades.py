#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    training_sessions = 0
    for _ in range(n):
        color = input().lower()
        if ("pink" in color) or ("rose" in color):
            training_sessions += 1
            
    if training_sessions == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(training_sessions)


if __name__ == '__main__':
    main()