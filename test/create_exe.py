#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import os
import shutil
import subprocess
import traceback

# Dictionary with the folders/files to remove
dict_folders_files = {
    'build': './build',
    'dist': './dist',
    'spec': 'test_problem.spec'
}

def cleaning_environment():
    '''
    Remove the files from the dict_folder_files.
    '''
    for item in dict_folders_files.values():
        try:
            if os.path.isfile(item):
                os.unlink(item)
            elif os.path.isdir(item):
                shutil.rmtree(item)
        except Exception:
            print(traceback.format_exc())
    


def create_exe():
    '''
    Use pyinstaller to create an executable of submit.
    '''
    list_of_args = ['pyinstaller', 'test_problem.py', '--onefile']
    print(subprocess.run(list_of_args, stdout=subprocess.PIPE).stdout.decode('uft-8'))


def copy_exe():
    '''
    Copy the executable to the root folder.
    '''
    shutil.copy(dict_folders_files['dist'] + '/test_problem.exe', './')


if __name__ == "__main__":
    cleaning_environment()

    create_exe()

    copy_exe()

    cleaning_environment()