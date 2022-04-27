#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    month, day = input().split()
    day = int(day)

    if (month == "OCT" and day == 31) or (month == "DEC" and day == 25):
        print("yup")
    else:
        print("nope")


if __name__ == "__main__":
    main()