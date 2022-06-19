#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def main():
    n = int(input())

    log = list()
    for _ in range(n):
        command, name = input().split()
        if command == "entry":
            if name in log:
                print(f"{name} entered (ANOMALY)")
            else:
                log.append(name)
                print(f"{name} entered")
            
        else:
            if name not in log:
                print(f"{name} exited (ANOMALY)")
            else:
                log.remove(name)
                print(f"{name} exited")


if __name__ == '__main__':
    main()