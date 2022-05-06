/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n, w, h, max_length, l;

    cin >> n >> w >> h;

    max_length = sqrt(pow(w, 2) + pow(h, 2));

    for (int i=0; i<n; i++) {
        cin >> l;

        if (l <= max_length) {
            cout << "DA" << endl;
        }
        else {
            cout << "NE" << endl;
        }
    }

    return 0;
}