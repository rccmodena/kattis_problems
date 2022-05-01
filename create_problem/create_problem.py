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
from bs4 import BeautifulSoup
import re


def main(problem_name):
    '''
    Compile the C source code
    '''
    base_website = "https://open.kattis.com/problems/"
    tests_website = base_website + f"{problem_name}/file/statement/samples.zip"
    problems_folder = r"D:\\my_stuff\\current\\sandbox\\kattis\\kattis\\problems\\"

    folder_name = problems_folder + problem_name[0] + r'\\' + problem_name + r'\\'
    test_folder_name = folder_name + r'tests\\'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.copyfile(problems_folder + 'base.c', folder_name + problem_name + '.c')
        shutil.copyfile(problems_folder + 'base.cpp', folder_name + problem_name + '.cpp')
        shutil.copyfile(problems_folder + 'base.py', folder_name + problem_name + '.py')

        with open(folder_name + problem_name + ".md", 'w', encoding="utf-8") as md_file:
            md_file.write(f"# {problem_name.upper()}\n\n")
            md_file.write(f"- [Problem Description]({base_website + problem_name})")

        os.makedirs(test_folder_name)
        tests_request = requests.get(tests_website)
        tests_zip = zipfile.ZipFile(io.BytesIO(tests_request.content))
        tests_zip.extractall(test_folder_name)

    else:
        print(F"Problem <{problem_name}> already created!")


if __name__ == '__main__':
    print("Type the name of the problem or NEXT to automatically find the next problem: ")
    problem_name = input().lower()

    if problem_name == "NEXT":
        print("Not implemented yet!")
    else:
        print(f"Do you want to create the problem: <{problem_name}>")
        print("Type YES to create.")
        create_problem = input()
        if create_problem == "YES":
            main(problem_name)
            print(f"Problem <{problem_name}> created with success!")
        else:
            print(f"Problem <{problem_name}> not created...")




