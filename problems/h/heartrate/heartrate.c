/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, b;
    float p, abpm, abpm_min, abpm_max, bpm;

    if (scanf("%d", &n) != 1) {
        printf("Failed to read n!");
    }

    for (int i=0; i<n; i++) {
        if (scanf("%d %f", &b, &p) != 2) {
            printf("Failed to read b and p!");
        }

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

        printf("%.4f %.4f %.4f\n", abpm_min, bpm, abpm_max);
    }

    return 0;
}