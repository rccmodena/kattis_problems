#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def distance_points(point_1, point_2):
    delta_x = abs(point_1[0] - point_2[0])
    delta_y = abs(point_1[1] - point_2[1])
    return (delta_x ** 2 + delta_y ** 2) ** (1/2)


def coordenates(patterns, value):
    coordenates = [0, 0]
    for i in range(3):
        if value in patterns[i]:
            coordenates[1] = i
            break
    coordenates[0] = patterns[coordenates[1]].index(value)

    return coordenates


def main():
    patterns = list()
    for i in range(3):
        patterns.append([int(val) for val in input().split()])

    previous_coordinates = None
    distance = 0
    for i in range(1, 10):
        if previous_coordinates is None:
            previous_coordinates = coordenates(patterns, i)
        else:
            distance += distance_points(previous_coordinates, coordenates(patterns, i))
            previous_coordinates = coordenates(patterns, i)

    print(distance)

if __name__ == '__main__':
    main()