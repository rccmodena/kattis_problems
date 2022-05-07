/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int g, s, c, total;

    if (scanf("%d %d %d\n", &g, &s, &c) != 3) {
        printf("Failed to read g, s and c!");
    }

    total = (g * 3) + (s * 2) + (c * 1);

    if (total >= 8) {
        printf("Province or ");
    }
    else if (total >= 5) {
        printf("Duchy or ");
    }
    else if (total >= 2) {
        printf("Estate or ");
    }

    if (total >= 6) {
        printf("Gold\n");
    }
    else if (total >= 3) {
        printf("Silver\n");
    }
    else {
        printf("Copper\n");
    }

    return 0;
}