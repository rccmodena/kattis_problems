/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;


double calc_euclidian_area(int radius) {
    return M_PI * pow(radius, 2);
}


double calc_taxicab_area(int radius) {
    return 2.0 * pow(radius, 2);
}

int main() {
    int r;

    cin >> r;

    cout << fixed;
    cout << setprecision(6);
    cout << calc_euclidian_area(r) << endl;
    cout << calc_taxicab_area(r) << endl;
}