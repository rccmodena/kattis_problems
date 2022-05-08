/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    string name;

    cin >> name;

    for (int i=0; name[i] != '\0'; i++) {
        if (i == 0) {
            cout << name[i];
        }
        else {
            if (name[i - 1] != name[i]) {
                cout << name[i];
            }
        }
    }
    cout << endl;
}