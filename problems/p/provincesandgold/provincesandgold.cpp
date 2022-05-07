/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int g, s, c, total;

    cin >> g >> s >> c;

    total = (g * 3) + (s * 2) + (c * 1);

    if (total >= 8) {
        cout << "Province or ";
    }
    else if (total >= 5) {
        cout << "Duchy or ";
    }
    else if (total >= 2) {
        cout << "Estate or ";
    }

    if (total >= 6) {
        cout << "Gold" << endl;
    }
    else if (total >= 3) {
        cout << "Silver" << endl;
    }
    else {
        cout << "Copper" << endl;
    }
}