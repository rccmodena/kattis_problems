/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int t, n, total_cities;
    bool repeated_city;
    
    cin >> t;

    for (int i=0; i<t; i++) {
        cin >> n;
        string cities[n];
        for (int j=0; j<n; j++) {
            cin >> cities[j];
        }
        total_cities = 1;
        for (int j=1; j<n; j++) {
            repeated_city = false;
            for (int k=0; k<j; k++) {
                if (cities[j] == cities[k]) {
                    repeated_city = true;
                    break;
                }
            }
            if (repeated_city == false) {
                total_cities++;
            }
        }
        cout << total_cities << endl;
    }
}