/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>

using namespace std;


double to_radians(double degrees) {
    return (degrees * M_PI ) / 180.0;
}

int main() {
    int h, v, ladder;

    cin >> h >> v;

    ladder = ceil(h / sin(to_radians(v)));

    cout << ladder << endl;
}