/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>
#include<cmath>

using namespace std;

int main() {
    int n, side, height, blocks;

    cin >> n;

    side = 1;
    height = 0;
    blocks = 1;

    while (n >= blocks) {
        n -= blocks;
        side += 2;
        blocks = pow(side, 2);
        height++;
    }

    cout << height << endl;

}