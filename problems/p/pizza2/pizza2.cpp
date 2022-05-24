/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double calc_area_circle(int radius) {
    return M_PI * pow(radius, 2);
}


int main() {
    int r, c;
    double total_area, total_cheese, percent_cheese;

    cin >> r >> c;

    total_area = calc_area_circle(r);
    total_cheese = calc_area_circle(r - c);
    percent_cheese = total_cheese / total_area * 100;

    cout << fixed;
    cout << setprecision(6);
    cout << percent_cheese << endl;
}