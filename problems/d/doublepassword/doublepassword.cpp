/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string s1, s2;
    int sequences = 1;

    cin >> s1;
    cin >> s2;

    for (size_t i=0; i<s1.length(); i++) {
        if (s1.at(i) == s2.at(i)) {
            sequences *= 1;
        }
        else {
            sequences *= 2;
        }
    }

    cout << sequences << endl;
}
