/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    const int SIZE_NUMBER = 7;
    const int SIZE_PREFIX = 3;

    char n[SIZE_NUMBER], result;
    if (scanf("%s", n) != 1) {
        printf("Failed to read n!");
    }

    result = 1;
    for (int i=0; i<SIZE_PREFIX; i++) {
        if (n[i] != '5') {
            result = 0;
            break;
        }
    }

    printf("%d", result);
}