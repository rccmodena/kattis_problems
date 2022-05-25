#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    marius_ah = input()
    doctor_ah = input()
    if len(marius_ah) >= len(doctor_ah):
        print("go")
    else:
        print("no")


if __name__ == '__main__':
    main()