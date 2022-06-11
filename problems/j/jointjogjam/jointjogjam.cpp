/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    double kari_start_x, kari_start_y, ola_start_x, ola_start_y, kari_end_x, kari_end_y, ola_end_x, ola_end_y, dist_1, dist_2;

    cin >> kari_start_x >> kari_start_y >> ola_start_x >> ola_start_y >> kari_end_x >> kari_end_y >> ola_end_x >> ola_end_y;

    dist_1 = sqrt(pow(kari_start_y - ola_start_y, 2) + pow(kari_start_x - ola_start_x, 2));
    dist_2 = sqrt(pow(kari_end_y - ola_end_y, 2) + pow(kari_end_x - ola_end_x, 2));
    
    cout << fixed;
    cout << setprecision(10);
    if (dist_1 > dist_2) {
        cout << dist_1 << endl;
    }
    else {
        cout << dist_2 << endl;
    }
}