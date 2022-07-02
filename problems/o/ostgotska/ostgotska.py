#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    list_words = input().split()
    n_words = len(list_words)
    max_ae = n_words * .4

    sum_ae_words = sum([1 for word in list_words if word.find("ae") != -1])

    if sum_ae_words >= max_ae:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")


if __name__ == '__main__':
    main()