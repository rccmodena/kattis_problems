#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    modulos = set()
    for _ in range(10):
        modulos.add(int(input()) % 42)

    print(len(modulos))


if __name__ == '__main__':
    main()