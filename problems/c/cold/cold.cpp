/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main() {
    int n, val, negative_t;

    cin >> n;

    negative_t = 0;
    for (int i=0; i<n; i++) {
        cin >> val;
        if (val < 0) {
            negative_t++;
        }
    }
    printf("%d\n", negative_t);
}