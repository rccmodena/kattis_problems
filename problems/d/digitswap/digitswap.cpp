/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string a;

    cin >> a;

    for (size_t i = a.length(); i-- > 0;) {
        cout << a.at(i);
    }
    cout << endl;
}