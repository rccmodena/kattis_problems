/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

#define NUMBERS_SEVEN_DWARVES 100
#define NUMBER_DWARVES 9

int main() {
    int dwarves[9];
    int total_dwarves, difference_dwarves, dwarf_number_1, dwarf_number_2;
    bool found_legit;

    total_dwarves = 0;
    for (int i=0; i<NUMBER_DWARVES; i++) {
        cin >> dwarves[i];
        total_dwarves += dwarves[i];
    }

    difference_dwarves = total_dwarves - NUMBERS_SEVEN_DWARVES;

    found_legit = false;

    dwarf_number_1 = 0;
    dwarf_number_2 = 0;
    
    for (int i=0; i<NUMBER_DWARVES; i++){
        dwarf_number_1 = dwarves[i];
        for (int j=0; j<NUMBER_DWARVES; j++) {
            if (i == j) {
                continue;
            }
            dwarf_number_2 = dwarves[j];

            if (dwarf_number_1 + dwarf_number_2 == difference_dwarves) {
                found_legit = true;
                break;
            }
        }
        if (found_legit) {
            break;
        }
    }

    for (int i=0; i<NUMBER_DWARVES; i++){
        if (dwarves[i] == dwarf_number_1 || dwarves[i] == dwarf_number_2) {
            continue;
        }
        cout << dwarves[i] << endl;
    }
}