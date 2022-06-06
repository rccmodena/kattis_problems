/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n, p, q, quocient;

    cin >> n >> p >> q;

    quocient = (p + q) / n;
    if (quocient % 2 == 0) {
        cout << "paul" << endl;
    }
    else {
        cout << "opponent" << endl;
    }
}