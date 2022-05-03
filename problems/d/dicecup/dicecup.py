#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n, m = [int(val) for val in input().split()]

    results = [0 for _ in (range(1, (n + m) + 2))]
    for outcome_a in range(1, n + 1):
        for outcome_b in range(1, m + 1):
            total = outcome_a + outcome_b
            results[total] += 1

    max_outcomes = max(results)
    for number, total in enumerate(results):
        if total == max_outcomes:
            print(number)


if __name__ == '__main__':
    main()