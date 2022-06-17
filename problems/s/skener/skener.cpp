/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int r, c, zr, zc;

    cin >> r >> c >> zr >> zc;
    cin.ignore();

    vector<string> matrix;
    for (int i=0;i<r;i++) {
        string line;
        getline(cin, line);
        matrix.push_back(line);
    }

    for (string line : matrix) {
        for (int row=0; row<zr; row++) {
           for (size_t col=0; col<line.size(); col++) {
                for (int r_col=0; r_col<zc; r_col++) {
                    cout << line[col];
                }
            }
            cout << endl;
        }
    }
}