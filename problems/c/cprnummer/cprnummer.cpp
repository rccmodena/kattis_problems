/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string cpr;
    string corresponding = "432765-4321";
    int cpr_sum = 0;

    cin >> cpr;

    for (size_t i=0; i<cpr.size(); i++) {
        if (cpr[i] == '-') {
            continue;
        }
        cpr_sum += (cpr[i] - 48) * (corresponding[i] - 48);
    }
    
    if (cpr_sum % 11 == 0) {
        cout << 1 << endl;
    }
    else {
        cout << 0 << endl;
    }
}