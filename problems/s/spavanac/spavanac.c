/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int h, m;
    if (scanf("%d %d", &h, &m) != 2) {
        printf("Failed to read h and m!");
    }

    if (m >= 45) {
        m -= 45;
    }
    else {
        if (h == 0) {
            h = 23;
        }
        else {
            h -= 1;
        }

        m = 60 + (m - 45);
    }

    printf("%d %d", h, m);

    return 0;
}