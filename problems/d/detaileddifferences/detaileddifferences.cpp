/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;

    cin >> n;
    cin.ignore();

    for (int i=0; i<n; i++) {
        string string_1, string_2;
        cin >> string_1;
        cin.ignore();
        cin >> string_2;
        cin.ignore();
        cout << string_1 << endl;
        cout << string_2 << endl;
        for (size_t i=0; i<string_1.size(); i++) {
            if (string_1[i] == string_2[i]) {
                cout << ".";
            }
            else {
                cout << "*";
            }
        }
        cout << endl << endl;
    }
}