/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) {
        printf("Failed to read a and b!");
    }

    if (a > b) {
        printf("%d %d", b, a);
    }
    else {
        printf("%d %d", a, b);
    }

    return 0;
}