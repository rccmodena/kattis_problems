/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int n, b;
    float p, abpm, abpm_min, abpm_max, bpm;

    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> b;
        cin >> p;

        if (p == 0) {
            abpm_min = 0;
            bpm = 0;
            abpm_max = 0;
        }
        else {
            abpm = 60 / p;
            bpm = 60 * b / p;
            abpm_min = bpm - abpm;
            abpm_max = bpm + abpm;
        }
        cout << fixed;
        cout << setprecision(4);
        cout << abpm_min << " " << bpm << " " << abpm_max << endl;
    }
}