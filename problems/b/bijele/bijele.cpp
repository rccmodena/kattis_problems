/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int k, q, r, b, n, p;

    cin >> k;
    cin >> q;
    cin >> r;
    cin >> b;
    cin >> n;
    cin >> p;

    // One king
    k = 1 - k;

    // One queen
    q = 1 - q;

    // Two rooks
    r = 2 - r;

    // Two bishops
    b = 2 - b;

    // Two knights
    n = 2 - n;

    // Eight pawns
    p = 8 - p;

    cout << k << " " << q << " " << r << " " << b << " " << n << " " << p << endl;
}