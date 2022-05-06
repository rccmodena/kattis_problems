/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    int count_card;
    string s;

    cin >> s;

    for (size_t i=0; i<s.length(); i++) {
        count_card = 0;
        for (size_t j=0; j<s.length(); j++) {
            if (s[i] == s[j]) {
                count_card++;
            }
            if (count_card > 1) {
                break;
            }
        }
        if (count_card > 1) {
            break;
        }
    }

    if (count_card > 1) {
        cout << 0 << endl;
    }
    else {
        cout << 1 << endl;
    }
}