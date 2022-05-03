/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>

int main(void) {
    int n, side, height, blocks;

    if (scanf("%d", &n) != 1) {
        printf("Failed to read n!");
    }

    side = 1;
    height = 0;
    blocks = 1;

    while (n >= blocks) {
        n -= blocks;
        side += 2;
        blocks = pow(side, 2);
        height++;
    }
    printf("%d", height);

    return 0;
}