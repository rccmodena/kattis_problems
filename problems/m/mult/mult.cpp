/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n, value, initial_number;

    cin >> n;

    initial_number = -1;
    for (int i=0; i<n; i++) {
        cin >> value;

        if (initial_number == -1) {
            initial_number = value;
            continue;
        }
        else {
            if (value % initial_number == 0) {
                cout << value << endl;
                initial_number = -1;
            }
        }

    }
}