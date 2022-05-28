/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>

#define CALORIES_PER_BOTTLE 400

using namespace std;

int main() {
    int t, n, n_bottles;

    cin >> t;

    for (int i=0; i<t; i++) {
        cin >> n;

        n_bottles = n / CALORIES_PER_BOTTLE;
        if (n % CALORIES_PER_BOTTLE > 0) {
            n_bottles++;
        }
        cout << n_bottles << endl;
    }
}