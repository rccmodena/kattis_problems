#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    t = int(input())

    for _ in range(t):
        list_turtles = [int(val) for val in input().split()]
        turtles_abroad = 0
        previous_turtles = 1
        for turtles in list_turtles[:-1]:
            if turtles > (previous_turtles * 2):
                turtles_abroad += turtles - (previous_turtles * 2)
            previous_turtles = turtles
        print(turtles_abroad)

if __name__ == '__main__':
    main()