#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())
    universities = list()
    universities_teams = list()
    for _ in range(n):
        university, team = input().split()
        if university not in universities:
            universities.append(university)
            universities_teams.append(university + " " + team)

    for i in range(12):
        print(universities_teams[i])


if __name__ == '__main__':
    main()