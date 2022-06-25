#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def format_hmz(hour):
    return [hour[0].zfill(5), hour[1]]

def sort_hours(list_hours):
    sorted_hours = list()
    while list_hours:
        smallest_hour_id = 0        
        smallest_hm, smallest_z = format_hmz(list_hours[smallest_hour_id])

        for id, hour in enumerate(list_hours):
            hm, z = format_hmz(hour)

            if z < smallest_z:
                smallest_hm = hm
                smallest_z = z
                smallest_hour_id = id
            elif z == smallest_z:
                if hm[:2] == '12':
                    if smallest_hm[:2] != hm[:2]:
                        smallest_hm = hm
                        smallest_z = z
                        smallest_hour_id = id
                    else:
                        if hm < smallest_hm:
                            smallest_hm = hm
                            smallest_z = z
                            smallest_hour_id = id
                if hm < smallest_hm and smallest_hm[:2] != '12':
                    smallest_hm = hm
                    smallest_z = z
                    smallest_hour_id = id

        hmz = list_hours.pop(smallest_hour_id)
        sorted_hours.append(" ".join(hmz))

    return sorted_hours

def main():
    while True:
        n = int(input())
        appointments = list()
        if n == 0:
            break
        for _ in range(n):
            appointments.append(input().split())

        for appointment in sort_hours(appointments):
            print(appointment)
        print('')


if __name__ == '__main__':
    main()