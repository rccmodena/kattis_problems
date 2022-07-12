#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def is_line_correct(line):
    n_white = 0
    n_black = 0
    sequence = {"type": "W", "count": 0}
    for square in line:
        if square == "W":
            n_white += 1

        if square == "B":
            n_black += 1

        if square == sequence["type"]:
            if sequence["count"] == 2:
                return False
            else:
                sequence["count"] += 1
        else:
            sequence["type"] = square
            sequence["count"] = 1

    if n_white == n_black:
        return True
    else:
        return False

def create_cols_list(line, cols_list):
    for i, square in enumerate(line):
        cols_list[i].append(square)
    return cols_list
         
 
def main():
    n = int(input())

    cols_list = [[] for n in range(n)]
    is_correct = True
    for _ in range(n):
        line = input()
        cols_list = create_cols_list(line, cols_list)
        if not is_line_correct(line):
            is_correct = False
            break

    if is_correct:
        for line in cols_list:
            if not is_line_correct(line):
                is_correct = False
                break

    if is_correct:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()