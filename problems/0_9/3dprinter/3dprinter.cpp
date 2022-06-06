/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, min_days, printers, days;

    cin >> n;

    min_days = n;

    for (int days_printer=2; days_printer<n; days_printer++) {
        printers = pow(2, days_printer - 1);
        days = ceil(n * 1.0 / printers * 1.0) + (days_printer - 1);

        if (days <= min_days) {
            min_days = days;
        }
        else {
            break;
        }
    }
    cout << min_days << endl;
}