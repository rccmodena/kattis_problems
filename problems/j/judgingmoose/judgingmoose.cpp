/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int l, r, points;

    cin >> l >> r;

    if (l == 0 && r == 0) {
        cout << "Not a moose";
    }
    else if (l != r) {
        points = 0;
        if (l > r) {
            points = l * 2;
        }
        else {
            points = r * 2;
        }
        cout << "Odd " << points;
    }
    else {
        cout << "Even " << l + r;
    }
}