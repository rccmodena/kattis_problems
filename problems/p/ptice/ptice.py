#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
dict_paterns = {
    "Adrian": "ABC",
    "Bruno": "BABC",
    "Goran": "CCAABB"
}

def main():
    n = int(input())
    correct_answers = input()

    dict_result = dict()
    max_score = 0
    for boy, pattern in dict_paterns.items():
        score = sum([1 for i,answer in enumerate(correct_answers) if answer == pattern[i % len(pattern)]])
        dict_result[boy] = score
        if score > max_score:
            max_score = score
    
    print(max_score)
    for boy, score in dict_result.items():
        if max_score == score:
            print(boy)


if __name__ == '__main__':
    main()
    