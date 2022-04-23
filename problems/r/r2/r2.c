/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int r1, r2, s;
    while (scanf("%d%d", &r1, &s) == 2)
        r2 = 2 * s - r1;
        printf("%d", r2);
    return 0;
}