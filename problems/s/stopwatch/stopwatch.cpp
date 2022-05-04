/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <iostream>

using namespace std;

int main(void) {
    int n, t, aux_t, sum_t;

    cin >> n;

    if (n % 2 == 0) {
        aux_t = 0;
        sum_t = 0;
        for (int i=0; i<n; i++) {
            cin >> t;
            if (i % 2 == 0) {
                aux_t = t;
            }
            else {
                sum_t += t - aux_t;
            }
        }
        printf("%d", sum_t);
    }
    else {
        for (int i=0; i<n; i++) {
        }
        printf("still running");
    }

    return 0;
}