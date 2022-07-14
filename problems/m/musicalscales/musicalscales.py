#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

MUSICAL_NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
MAJOR_SCALE = [2, 2, 1, 2, 2, 2, 1]

def main():
    n = int(input())

    sequence_notes = input().split()

    list_scales_ouput = []
    for i_note in range(len(MUSICAL_NOTES)):
        scale = [MUSICAL_NOTES[i_note]]
        last_i_note = i_note
        for diff in MAJOR_SCALE:
            current_i_note = (last_i_note + diff) % len(MUSICAL_NOTES)
            scale.append(MUSICAL_NOTES[current_i_note])
            last_i_note += diff

        song_use_this_scale = True
        for note in sequence_notes:
            if note not in scale:
                song_use_this_scale = False
                break
        
        if song_use_this_scale:
            list_scales_ouput.append(MUSICAL_NOTES[i_note])

    if list_scales_ouput:
        print(*list_scales_ouput)
    else:
        print("none")


if __name__ == '__main__':
    main()