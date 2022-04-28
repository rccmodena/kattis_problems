/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string s, r;

    cin >> s;

    size_t n_e = count(s.begin(), s.end(), 'e');


    s = "h";

    for (size_t i=0; i<(n_e * 2); i++) {
        s.append("e");
    }
    s.append("y");

    cout << s << endl;
}