/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

#define CALORIES_PER_BOTTLE 400

int main(void) {
    int t, n, n_bottles;

    if (scanf("%d", &t) != 1) {
        printf("Failed to read t!");
    }

    for (int i=0; i<t; i++) {
        if (scanf("%d", &n) != 1) {
            printf("Failed to read n!");
        }

        n_bottles = n / CALORIES_PER_BOTTLE;
        if (n % CALORIES_PER_BOTTLE > 0) {
            n_bottles++;
        }
        
        printf("%d\n", n_bottles);
    }

    return 0;
}