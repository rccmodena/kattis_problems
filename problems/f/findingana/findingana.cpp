/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string s, result;
    int suffix_ini, length;

    cin >> s;
    suffix_ini = s.find('a');
    length = s.length();

    result = s.substr(suffix_ini, (length - suffix_ini));

    cout << result << endl;
}