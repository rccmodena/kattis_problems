#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    numbers_seven_dwarves = 100
    dwarves = list()
    for _ in range(9):
        dwarves.append(int(input()))

    total_dwarves = sum(dwarves)
    difference_dwarves = total_dwarves - numbers_seven_dwarves

    found_legit = False
    for i in range(9):
        value_1 = dwarves[i]
        for j in range(9):
            if i == j:
                continue
            value_2 = dwarves[j]
            if value_1 + value_2 == difference_dwarves:
                found_legit = True
                dwarves.remove(value_1)
                dwarves.remove(value_2)
                break

        if found_legit:
            break

    for dwarf in dwarves:
        print(dwarf)


if __name__ == '__main__':
    main()