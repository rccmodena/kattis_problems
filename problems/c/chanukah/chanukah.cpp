/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int p, k, n, candles;

    cin >> p;

    for (int i=0; i<p; i++) {
        cin >> k;
        cin >> n;

        candles = 0;
        for (int j=1; j<n+1; j++) {
            candles += j + 1;
        }

        cout << k << " " << candles << endl;

    }

    
}