/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int g, t, n, towing, towing_90, wi, w_sum, result;

    cin >> g;
    cin >> t;
    cin >> n;

    towing = g - t;
    towing_90 = static_cast<int>(towing * 0.9);

    w_sum = 0;
    for (int i=0; i<n; i++) {
        cin >> wi;
        
        w_sum += wi;
    }

    result = towing_90 - w_sum;

    cout << result << endl;
}