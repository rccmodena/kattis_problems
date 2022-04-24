/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int a, b;
    if (scanf("%d%d", &a, &b) != 2) {
        printf("Failed to read a and b!");
    }

    printf("%d", a + b);

    return 0;
}