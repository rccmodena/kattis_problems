#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def get_list_int():
    return  [int(val) for val in input().split()]
def main():
    n = int(input())

    max_speed = 0
    previous_t, previous_d = get_list_int()
    for i in range(n - 1):
        t, d = get_list_int()
        speed = (d - previous_d) // (t - previous_t)
        if speed > max_speed:
            max_speed = speed
        previous_t = t
        previous_d = d

    print(max_speed)


if __name__ == '__main__':
    main()