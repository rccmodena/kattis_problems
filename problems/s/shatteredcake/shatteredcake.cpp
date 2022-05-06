/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int w, n, wi, li, area;

    cin >> w;
    cin >> n;

    area = 0;
    for (int i=0; i<n; i++) {
        cin >> wi >> li;
        area +=  wi * li;
    }

    cout << area/w << endl;
}