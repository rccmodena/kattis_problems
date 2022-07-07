#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    a, b, c = [int(val) for val in input().split()]

    list_operations_1 = ["==", "+", "-", "*", "/"]
    list_operations_2 = list_operations_1[1:].copy()
    found_equation = False
    for op1 in list_operations_1:
        for op2 in list_operations_2:
            if eval(f"a {op1} b {op2} c"):
                if op1 == "==":
                    print(f"{a}={b}{op2}{c}")
                else:
                    print(f"{a}{op1}{b}={c}")
                found_equation = True
                break
        if found_equation:
            break
        if op1 == "==":
            list_operations_2 = ["=="]


if __name__ == '__main__':
    main()