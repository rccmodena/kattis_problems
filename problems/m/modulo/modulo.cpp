/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

#define SIZE_LIST 10

int main() {
    int number;
    set<int, greater<int> > set_modulo;

    for (int i=0; i<SIZE_LIST; i++) {
        cin >> number;
        set_modulo.insert(number % 42);
    }

    cout << set_modulo.size() << endl;
}