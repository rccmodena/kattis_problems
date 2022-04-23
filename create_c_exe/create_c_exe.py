#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import sys
import subprocess


def main(source_name):
    '''
    Compile the C source code
    '''
    args_list = ['gcc', '-g', '-O2', '-std=gnu11', '-static', f'{source_name}.c', '-lm', '-o', f'{source_name}.exe']
    result = (subprocess.run(args_list, stdout=subprocess.PIPE, encoding='utf-8').stdout).strip()

if __name__ == '__main__':
    # Create variable with arguments
    source_name = sys.argv[1]

    # main function
    main(source_name)