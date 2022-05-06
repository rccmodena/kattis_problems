/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n, number, total;

    cin >> n;

    total = 0;
    for (int i=0; i<n; i++) {
        cin >> number;
        total += number;
    }

    cout << total << endl;
}