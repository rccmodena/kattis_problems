#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    _ = input()
    bricks = [int(val) for val in input().split()]

    total_towers = 1
    previous_brick = bricks[0]
    for brick in bricks[1:]:
        if brick > previous_brick:
            total_towers += 1
        previous_brick = brick

    print(total_towers)


if __name__ == '__main__':
    main()