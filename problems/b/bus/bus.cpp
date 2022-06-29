/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, stops;

    cin >> t;
    cin.ignore();

    for(int i=0; i<t; i++) {
        cin >> stops;
        cin.ignore();
        int current_number_passengers = 0;
        for(int j=0; j<stops; j++) {
            current_number_passengers = (current_number_passengers + 0.5) * 2;
        }
        cout << current_number_passengers << endl;
    }
}