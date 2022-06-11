#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    kari_start_x, kari_start_y, ola_start_x, ola_start_y, kari_end_x, kari_end_y, ola_end_x, ola_end_y = [int(val) for val in input().split()]

    dist_1 = ((kari_start_y - ola_start_y) ** 2 + (kari_start_x - ola_start_x) ** 2) ** (1/2)
    dist_2 = ((kari_end_y - ola_end_y) ** 2 + (kari_end_x - ola_end_x) ** 2) ** (1/2)
    
    if dist_1 > dist_2:
        print(round(dist_1, 10))
    else:
        print(round(dist_2, 10))


if __name__ == '__main__':
    main()