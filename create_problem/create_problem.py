#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import sys
import os
import shutil


def main(problem_name):
    '''
    Compile the C source code
    '''
    problems_folder = r"D:\\my_stuff\\current\\sandbox\\kattis\\kattis\\problems\\"

    folder_name = problems_folder + problem_name[0] + r'\\' + problem_name + r'\\'

    if not os.path.exists(folder_name):
        pass
        os.makedirs(folder_name)
        shutil.copyfile(problems_folder + 'base.c', folder_name + problem_name + '.c')
        shutil.copyfile(problems_folder + 'base.cpp', folder_name + problem_name + '.cpp')
        shutil.copyfile(problems_folder + 'base.md', folder_name + problem_name + '.md')
        shutil.copyfile(problems_folder + 'base.py', folder_name + problem_name + '.py')
    else:
        print(F"Problem <{problem_name}> already created!")


if __name__ == '__main__':
    print("Type the name of the problem: ")
    problem_name = input().lower()

    print(f"Do you want to create the problem: <{problem_name}>")
    print("Type YES to create.")
    create_problem = input()
    if create_problem == "YES":
        main(problem_name)