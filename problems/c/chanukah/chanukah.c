/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int p, k, n, candles;
    if (scanf("%d", &p) != 1) {
        printf("Failed to read p!");
    }

    for (int i=0; i<p; i++) {
        if (scanf("%d%d", &k, &n) != 2) {
            printf("Failed to read k and n!");
        }

        candles = 0;
        for (int j=1; j<n+1; j++) {
            candles += j + 1;
        }

        printf("%d %d\n", k, candles);
    }

    return 0;
}