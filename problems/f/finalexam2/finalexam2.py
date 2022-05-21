#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    answers = [input() for _ in range(n)]

    print(sum([1 for i in range(n - 1) if answers[i] == answers[i + 1]]))


if __name__ == '__main__':
    main()