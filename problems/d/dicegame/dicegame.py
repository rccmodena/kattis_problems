#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    gunnar_dice = [int(val) for val in input().split()]
    emma_dice = [int(val) for val in input().split()]

    gunnar_sum = ((gunnar_dice[0] + gunnar_dice[1]) / 2) + ((gunnar_dice[2] + gunnar_dice[3]) / 2)
    emma_sum = ((emma_dice[0] + emma_dice[1]) / 2) + ((emma_dice[2] + emma_dice[3]) / 2)

    if gunnar_sum == emma_sum:
        print("Tie")
    elif gunnar_sum > emma_sum:
        print("Gunnar")
    else:
        print("Emma")


if __name__ == '__main__':
    main()