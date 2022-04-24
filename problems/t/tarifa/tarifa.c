/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int x, n, p, internet;

    if (scanf("%d", &x) != 1) {
        printf("Failed to read x!");
    }

    if (scanf("%d", &n) != 1) {
        printf("Failed to read n!");
    }

    internet = x;

    for (int i=0; i<n; i++) {
        if (scanf("%d", &p) != 1) {
            printf("Failed to read p!");
        }
        else {
            internet += (x - p);
        }
    }

    printf("%d", internet);

    return 0;
}