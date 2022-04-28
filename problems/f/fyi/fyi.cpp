/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string n, prefix;

    cin >> n;
    prefix = n.substr (0,3);

    if (prefix == "555") {
        cout << 1 << endl;
    }
    else {
        cout << 0 << endl;
    }

}