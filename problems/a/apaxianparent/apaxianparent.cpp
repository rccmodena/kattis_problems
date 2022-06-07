/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string y, p, y_end;

    cin >> y >> p;

    y_end = y.substr(y.size()-2, 2);

    if (y_end == "ex") {
        cout << y << p << endl;
    }
    else if (y_end[1] == 'e') {
        cout << y << 'x' << p << endl;
    }
    else if (y_end[1] == 'a' || y_end[1] == 'i' || y_end[1] == 'o' || y_end[1] == 'u') {
        cout << y.substr(0, y.size() - 1) << "ex" << p << endl;
    }
    else {
        cout << y << "ex" << p << endl;
    }
}