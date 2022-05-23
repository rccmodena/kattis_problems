#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    dict_birthdays = dict()
    for _ in range(n):
        s, c, birth = input().split()

        if dict_birthdays.get(birth) is None:
            dict_birthdays[birth] = {'name': s, 'like': int(c)}
        else:
            if int(c) > dict_birthdays[birth].get('like'):
                dict_birthdays[birth] = {'name': s, 'like': int(c)}

    list_friends = []
    for birth in dict_birthdays:
        list_friends.append(dict_birthdays[birth].get('name'))

    print(len(list_friends))

    for friend in sorted(list_friends):
        print(friend)

if __name__ == '__main__':
    main()