/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int sweet, sour;

    while (true) {
        cin >> sweet >> sour;

        if (sweet == 0 && sour == 0) {
            break;
        }
        else if (sweet == sour) {
            cout << "Undecided." << endl;
        }
        else if (sweet + sour == 13) {
            cout << "Never speak again." << endl;
        }
        else if (sweet > sour) {
            cout << "To the convention." << endl;
        }
        else {
            cout << "Left beehind." << endl;
        }
    }
}