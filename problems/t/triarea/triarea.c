/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int a, b;
    float triangle_area;
    if (scanf("%d%d", &a, &b) != 2) {
        printf("Failed to read a and b!");
    }

    triangle_area = (a * b) / 2.0;

    printf("%f", triangle_area);

    return 0;
}