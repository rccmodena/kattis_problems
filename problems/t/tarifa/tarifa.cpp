/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int x, n, p, internet;

    cin >> x;
    cin >> n;

    internet = x;

    for (int i=0; i < n; i++) {
        cin >> p;
        internet += (x - p);
    }

    cout << internet << endl;
}