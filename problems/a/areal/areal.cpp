/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double area, fence_length;

    cin >> area;

    fence_length = 4.0 * sqrt(area);

    cout << fixed;
    cout << setprecision(8);
    cout << fence_length << endl;
}