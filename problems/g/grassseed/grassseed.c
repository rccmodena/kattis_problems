/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    double c, cost_lawns, wi, li;
    int l;

    if (scanf("%lf", &c) != 1) {
        printf("Failed to read c!");
    }

    if (scanf("%d", &l) != 1) {
        printf("Failed to read l!");
    }

    cost_lawns = 0;
    for (int i=0; i<l; i++) {
        if (scanf("%lf%lf", &wi, &li) != 2) {
            printf("Failed to read wi and li!");
        }

        cost_lawns += wi * li * c;
    }

    printf("%.7lf", cost_lawns);

    return 0;
}