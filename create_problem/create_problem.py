#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import os
import shutil
import requests
import zipfile
import io


def main(problem_name):
    '''
    Compile the C source code
    '''
    tests_website = f"https://open.kattis.com/problems/{problem_name}/file/statement/samples.zip"
    problems_folder = r"D:\\my_stuff\\current\\sandbox\\kattis\\kattis\\problems\\"

    folder_name = problems_folder + problem_name[0] + r'\\' + problem_name + r'\\'
    test_folder_name = folder_name + r'tests\\'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.copyfile(problems_folder + 'base.c', folder_name + problem_name + '.c')
        shutil.copyfile(problems_folder + 'base.cpp', folder_name + problem_name + '.cpp')
        shutil.copyfile(problems_folder + 'base.md', folder_name + problem_name + '.md')
        shutil.copyfile(problems_folder + 'base.py', folder_name + problem_name + '.py')

        os.makedirs(test_folder_name)
        tests_request = requests.get(tests_website)
        tests_zip = zipfile.ZipFile(io.BytesIO(tests_request.content))
        tests_zip.extractall(test_folder_name)

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
        print(f"Problem <{problem_name}> created with success!")
    else:
        print(f"Problem <{problem_name}> not created...")
