/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n, h, v, volume;

    cin >> n >> h >> v;

    volume = 4;

    if (h > n - h) {
        volume *= h;
    }
    else {
        volume *= (n - h);
    }

    if (v > n - v)  {
        volume *= v;
    }
    else {
        volume *= (n - v);
    }

    cout << volume << endl;
}