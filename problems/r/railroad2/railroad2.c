/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int x, y;

    if (scanf("%d %d", &x, &y) != 2) {
        printf("Failed to read x and y!");
    }
    
    if (y % 2 == 0) {
        printf("possible");
    }
    else {
        printf("impossible");
    }

    return 0;
}