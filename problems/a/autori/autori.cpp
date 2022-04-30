/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    int first_letter = 1;
    string long_naming;

    cin >> long_naming;

    for (size_t i=0; i<long_naming.length();i++) {
        if (first_letter == 1) {
            cout << long_naming[i];
            first_letter = 0;
        }
        else {
            if (long_naming[i] == '-') {
                first_letter = 1;
            }
        }
    }
}