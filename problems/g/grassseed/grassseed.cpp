/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double c, cost_lawns, wi, li;
    int l;

    cin >> c;
    cin >> l;

    cost_lawns = 0;
    for (int i=0; i<l; i++) {
        cin >> wi;
        cin >> li;

        cost_lawns += wi * li * c;
    }

    cout << fixed;
    cout << setprecision(7);
    cout << cost_lawns << endl;
}