#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n  = int(input())
    transformed_a = [int(val) for val in input().split()]

    list_valid = [0] * n
    max_value = transformed_a[0]
    min_value = transformed_a[-1]
    for i in range(n):
        pivot_left = transformed_a[i]
        if pivot_left >= max_value:
            list_valid[i] += 1
            max_value = pivot_left

        last_index = n - (i + 1)
        pivot_right = transformed_a[last_index]
        if pivot_right <= min_value:
            list_valid[last_index] += 1
            min_value = pivot_right

    print(sum([1 if val == 2 else 0 for val in list_valid]))


if __name__ == '__main__':
    main()