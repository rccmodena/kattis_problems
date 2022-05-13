/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int a, b, c, space_1, space_2;

    cin >> a >> b >> c;

    space_1 = b - a;
    space_2 = c - b;

    if (space_1 > space_2) {
        cout << space_1 - 1 << endl;
    }
    else {
        cout << space_2 - 1 << endl;
    }
}