/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, bases;
    double slugging_sum, slugging_percentage;

    cin >> n;

    int numbers[n];

    for (int i=0; i<n; i++) {
        cin >> numbers[i];
    }

    slugging_sum = 0;
    bases = n;
    for (int i=0; i<n; i++) {
        if (numbers[i] == -1) {
            bases--;
        }
        else {
            slugging_sum += numbers[i];
        }
    }

    slugging_percentage = slugging_sum / bases;

    cout << slugging_percentage << endl;
}