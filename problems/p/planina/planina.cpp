/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int n, points;

    cin >> n;

    // Start with 2, and then add powers of 2
    points = 2;
    for (int power=0; power<n; power++){
        points += pow(2, power);
    }
    points = pow(points, 2);

    cout << points << endl;

}