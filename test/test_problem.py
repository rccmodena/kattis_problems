#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import sys
import os
import subprocess


def main(problem, tests_folder):
    '''
    Run the tests
    '''
    for file in os.listdir(tests_folder):
        if file[-3:] == '.in':
            with open('tests/' + file, 'r') as content_file:
                inputs = content_file.read()

            with open('tests/' + file[:-3] +'.ans', 'r') as content_file:
                outputs = content_file.read().strip()

            if problem[-3:] == ".py":
                result = (subprocess.run(['python', problem], input=inputs, stdout=subprocess.PIPE, encoding='utf-8').stdout).strip()
            else:
                result = (subprocess.run([problem], input=inputs, stdout=subprocess.PIPE, encoding='utf-8').stdout).strip()

            if result != outputs:
                print(f'Test n.: {file[-3:]}, Result: {result}, Expected: {outputs}')
                break
    else:
        print("All tests passed!")


if __name__ == '__main__':
    # Create variable with arguments
    problem = sys.argv[1]
    tests_folder = sys.argv[2]

    # main function
    main(problem, tests_folder)