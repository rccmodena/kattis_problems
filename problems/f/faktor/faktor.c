/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int a, i, scientists;
    if (scanf("%d%d", &a, &i) != 2) {
        printf("Failed to read a and i!");
    }

    scientists = a * (i - 1) + 1;

    printf("%d", scientists);

    return 0;
}