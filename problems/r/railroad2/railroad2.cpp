/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int x, y;

    cin >> x >> y;

    if (y % 2 == 0) {
        cout << "possible" << endl;
    }
    else {
        cout << "impossible" << endl;
    }
}