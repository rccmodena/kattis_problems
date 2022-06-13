#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    books = list()
    for _ in range(n):
        books.append(int(input()))
    
    books.sort(reverse=True)
    print(sum([book for i, book in enumerate(books) if i % 3 != 2]))


if __name__ == '__main__':
    main()