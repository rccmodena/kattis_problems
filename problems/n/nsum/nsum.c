/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int n, number, total;
    if (scanf("%d\n", &n) != 1) {
        printf("Failed to read n!");
    }

    total = 0;
    for (int i=0; i<n; i++) {
        if (scanf("%d ", &number) != 1) {
            printf("Failed to read number!");
        }
        total += number;
    }

    printf("%d", total);

    return 0;
}