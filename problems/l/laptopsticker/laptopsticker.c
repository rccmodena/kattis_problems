/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int wc, hc, ws, hs;
    if (scanf("%d %d %d %d\n", &wc, &hc, &ws, &hs) != 4) {
        printf("Failed to read wc, hc, ws and hs!");
    }

    if ((ws + 2 <= wc ) && (hs + 2 <= hc)) {
        printf("1");
    }
    else {
        printf("0");
    }

    return 0;
}