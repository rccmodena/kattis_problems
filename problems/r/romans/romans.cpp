/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    float x;
    int roman;

    cin >> x;

    roman = round(x * 1000 * 5280/4854);

    cout << roman << endl;
}