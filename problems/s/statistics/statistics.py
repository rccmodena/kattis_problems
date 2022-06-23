#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    i = 1
    while True:
        try:
            list_input = [int(val) for val in input().split()][1:]
            min_value = min(list_input)
            max_value = max(list_input)
            print(f"Case {i}: {min_value} {max_value} {max_value - min_value}")
            i += 1

        except EOFError:
            break


if __name__ == '__main__':
    main()