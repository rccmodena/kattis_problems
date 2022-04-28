/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int g, t, n, towing, towing_90, wi, w_sum, result;
    if (scanf("%d%d%d", &g, &t, &n) != 3) {
        printf("Failed to read g, t and n!");
    }

    towing = g - t;
    towing_90 = (int)(towing * 0.9);

    w_sum = 0;
    for (int i=0; i<n; i++) {
        if (scanf("%d", &wi) != 1) {
            printf("Failed to read wi!");
        }
        w_sum += wi;
    }

    result = towing_90 - w_sum;

    printf("%d\n", result);

    return 0;
}