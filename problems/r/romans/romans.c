/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>

int main(void) {
    float x;
    int roman;

    if (scanf("%f", &x) != 1) {
        printf("Failed to read x!");
    }

    roman = roundf(x * 1000 * 5280/4854);

    printf("%d", roman);

    return 0;
}