/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, t, aux_t, sum_t;
    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    if (n % 2 == 0) {
        aux_t = 0;
        sum_t = 0;
        for (int i=0; i<n; i++) {
            if (scanf("%d\n", &t) != 1) {
                printf("Failed to read t!");
            }
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