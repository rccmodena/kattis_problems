/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int k, q, r, b, n, p;

    if (scanf("%d %d %d %d %d %d\n", &k, &q, &r, &b, &n, &p) != 6) {
        printf("Failed to read the pieces!");
    }

    // One king
    k = 1 - k;

    // One queen
    q = 1 - q;

    // Two rooks
    r = 2 - r;

    // Two bishops
    b = 2 - b;

    // Two knights
    n = 2 - n;

    // Eight pawns
    p = 8 - p;

    printf("%d %d %d %d %d %d", k, q, r, b, n, p);

    return 0;
}