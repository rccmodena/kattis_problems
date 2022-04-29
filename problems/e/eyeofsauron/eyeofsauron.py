#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = input()

    result = "correct"

    if len(n) % 2 == 1:
        result = "fix"

    else:
        list_n = list(n)

        while list_n:
            left = list_n.pop(0)
            right = list_n.pop(-1)

            if left != right:
                if left == '(' and right == ')':
                    result = "correct"

                else:
                    result = "fix"

    print(result)


if __name__ == '__main__':
    main()