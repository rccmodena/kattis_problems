/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int l, r, points;

    if (scanf("%d %d", &l, &r) != 2) {
        printf("Failed to read l and r!");
    }

    if (l == 0 && r == 0) {
        printf("Not a moose");
    }
    else if (l != r) {
        points = 0;
        if (l > r) {
            points = l * 2;
        }
        else {
            points = r * 2;
        }
        printf("Odd %d", points);
    }
    else {
        printf("Even %d", l + r);
    }

    return 0;
}