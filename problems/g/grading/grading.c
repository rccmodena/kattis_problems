/*
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
*/

#include <stdio.h>

int main(void) {
    int a, b, c, d, e, score;

    if (scanf("%d %d %d %d %d\n", &a, &b, &c, &d, &e) != 5) {
        printf("Failed to read thresholds!");
    }

    if (scanf("%d\n", &score) != 1) {
        printf("Failed to read score!");
    }

    if (score >= a) {
        printf("A");
    }
    else if (score >= b) {
        printf("B");
    }
    else if (score >= c) {
        printf("C");
    }
    else if (score >= d) {
        printf("D");
    }
    else if (score >= e) {
        printf("E");
    }
    else {
        printf("F");
    }

    return 0;
}