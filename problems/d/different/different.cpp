/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string line;
    while (getline(cin, line)) {
        stringstream ss(line);
        unsigned long long a, b;
        ss >> a >> b;

        long long difference = a - b;

        cout << abs(difference) << endl;
    }
}