/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <bits/stdc++.h>

using namespace std;

double calc_root_derivative(int X, int Y) {
    int threshold;

    if (X < Y) {
        threshold = X / 2.0;
    }
    else {
        threshold = Y / 2.0;
    }

    int a = 12.0;
    int b = (-4.0 * X) + (-4.0 * Y);
    int c = X * Y;
    double delta = pow(b, 2.0) - 4.0 * a * c;
    double root_1 = ((- 1.0 * b) + sqrt(delta)) / (2.0 * a);
    double root_2 = ((- 1.0 * b) - sqrt(delta)) / (2.0 * a);  

    if (0 < root_1 && root_1 < threshold) {
        return root_1;
    }
    else {
        return root_2;
    }
}


double calc_volume(double h, int X, int Y) {
    return (4.0 * pow(h, 3.0)) - (2.0 * X * pow(h, 2.0)) - (2.0 * Y * pow(h, 2.0)) + (X * Y * h);
}


int main() {
    int t, X, Y;
    double h;

    cin >> t;

    cout << fixed;
    cout << setprecision(10);

    for (int i=0; i<t; i++) {
        cin >> X >> Y;

        h = calc_root_derivative(X, Y);

        cout << calc_volume(h, X, Y) << endl;
    }
}