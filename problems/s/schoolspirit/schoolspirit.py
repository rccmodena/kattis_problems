#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def calc_score(list_users):
    CONST_1 = 1/5
    CONST_2 = 4/5
    score = 0
    for i, user in enumerate(list_users):
        score += user * (CONST_2 ** i)
    return CONST_1 * score


def average_missing_student(list_users):
    scores_list = list()
    for del_id in range(len(list_users)):
        scores_list.append(calc_score([user for i, user in enumerate(list_users) if i != del_id]))
    return sum(scores_list) / len(scores_list)


def main():
    n = int(input())

    students_list = [int(input()) for _ in range(n)]

    print(calc_score(students_list))
    print(average_missing_student(students_list))


if __name__ == '__main__':
    main()