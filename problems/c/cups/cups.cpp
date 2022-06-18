/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    int radius;
    string color;
    map<int, string> tokens;

    cin >> n;
    cin.ignore();

    for (int i=0; i<n; i++) {
        for (int j=0; j<2; j++) {
            string token;
            stringstream ss;
            int val;

            cin >> token;
            ss << token;

            if (ss >> val) {
                if (j == 0) {
                    radius = val / 2;
                }
                else {
                    radius = val;
                }
            }
            else {
                color = token;
            }
        }
        tokens[radius] = color;
    }

    for (pair<int, string> x : tokens)
    {
        cout << x.second << endl;
    }
}