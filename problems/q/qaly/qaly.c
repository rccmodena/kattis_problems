/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n;
    float q, y, qaly;
    if (scanf("%d", &n) != 1) {
        printf("Failed to read n!");
    }

    qaly = 0;
    for (int i=0; i<n; i++) {
        if (scanf("%f%f", &q, &y) != 2) {
            printf("Failed to read q and y!");
        }
        qaly += q * y;
    }

    printf("%.3f", qaly);

    return 0;
}