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


# PATHS
BASE_WEBSITE = "https://open.kattis.com/problems/"
PROBLEMS_FOLDER = r"D:\\my_stuff\\current\\sandbox\\kattis\\kattis\\problems\\"
PROBLEMS_WEBSITE_0 = "https://open.kattis.com/problems?order=problem_difficulty"
PROBLEMS_WEBSITE_N = "https://open.kattis.com/problems?page={i}&order=problem_difficulty"


def get_next_problem():
    '''
    Get the name of the next problem
    '''
    for i in range(10):
        if i == 0:
            page = requests.get(PROBLEMS_WEBSITE_0)
        else:
            page = requests.get(PROBLEMS_WEBSITE_N.format(i=i))

        soup = BeautifulSoup(page.content, 'html.parser')
        table_content = soup.find_all("td",  {"class": "name_column"})

        for table in table_content:
            problem_name = table.find('a').get('href').split('/')[-1]
            folder_name = PROBLEMS_FOLDER + problem_name[0] + r'\\' + problem_name + r'\\'

            if not os.path.exists(folder_name):
                return problem_name
    else:
        print("All of the problems from the first page are done!")
        problem_name = None

    return problem_name


def main(problem_name):
    '''
    Create the structure of the problem
    '''
    TESTS_WEBSITE = BASE_WEBSITE + f"{problem_name}/file/statement/samples.zip"

    folder_name = PROBLEMS_FOLDER + problem_name[0] + r'\\' + problem_name + r'\\'
    test_folder_name = folder_name + r'tests\\'

    if not os.path.exists(folder_name):
        try:
            tests_request = requests.get(TESTS_WEBSITE)
        except Exception as e:
            return False

        if tests_request.status_code == 404:
            return False
        else:
            os.makedirs(folder_name)
            shutil.copyfile(PROBLEMS_FOLDER + 'base.c', folder_name + problem_name + '.c')
            shutil.copyfile(PROBLEMS_FOLDER + 'base.cpp', folder_name + problem_name + '.cpp')
            shutil.copyfile(PROBLEMS_FOLDER + 'base.py', folder_name + problem_name + '.py')

            with open(folder_name + problem_name + ".md", 'w', encoding="utf-8") as md_file:
                md_file.write(f"# {problem_name.upper()}\n\n")
                md_file.write(f"- [Problem Description]({BASE_WEBSITE + problem_name})")

            os.makedirs(test_folder_name)
            tests_zip = zipfile.ZipFile(io.BytesIO(tests_request.content))
            tests_zip.extractall(test_folder_name)
            return True

    else:
        print(F"Problem <{problem_name}> already created!")
        return False


if __name__ == '__main__':
    print("Type the name of the problem or NEXT to automatically find the next problem: ")
    problem_name = input()

    if problem_name == "NEXT":
        problem_name = get_next_problem()

    if problem_name is not None:
        problem_name = problem_name.lower()
        print(f"Do you want to create the problem: <{problem_name}>")
        print("Type YES to create.")
        create_problem = input()
        if create_problem == "YES":
            if main(problem_name):
                print(f"Problem <{problem_name}> created with success!")
            else:
                print(f"Problem <{problem_name}> not created...")    
        else:
            print(f"Problem <{problem_name}> not created...")
