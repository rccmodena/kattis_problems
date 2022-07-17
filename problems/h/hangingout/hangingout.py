#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    L, x = [int(val) for val in input().split()]

    n_people_terrace = 0
    n_groups_denied = 0
    for _ in range(x):
        line = input().split()
        event = line[0]
        p = int(line[1])

        if event == "enter":
            calc_n_people = n_people_terrace + p
        else:
            calc_n_people = n_people_terrace - p

        if calc_n_people > L:
            n_groups_denied += 1
        else:
            n_people_terrace = calc_n_people

    print(n_groups_denied)


if __name__ == '__main__':
    main()