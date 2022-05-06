/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>
#include <math.h>

int main(void) {
    int n, w, h, max_length, l;
    if (scanf("%d %d %d\n", &n, &w, &h) != 3) {
        printf("Failed to read n, w and h!");
    }

    max_length = sqrt(pow(w, 2) + pow(h, 2));

    for (int i=0; i<n; i++) {
        if (scanf("%d\n", &l) != 1) {
            printf("Failed to read l!");
        }
        if (l <= max_length) {
            printf("DA\n");
        }
        else {
            printf("NE\n");
        }
    }

    return 0;
}