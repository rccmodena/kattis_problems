/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int n;
    float q, y, qaly;

    cin >> n;

    qaly = 0;
    for (int i=0; i<n; i++) {
        cin >> q;
        cin >> y;

        qaly += q * y;
    }
    cout << fixed;
    cout << setprecision(3);
    cout << qaly;
}